# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4494?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4494
- Title: American Cures Act
- Congress: 119
- Bill type: S
- Bill number: 4494
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-15T18:42:22Z
- Update date including text: 2026-05-15T18:42:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Appropriations. (text: CR S2239)
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Appropriations. (text: CR S2239)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4494",
    "number": "4494",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "American Cures Act",
    "type": "S",
    "updateDate": "2026-05-15T18:42:22Z",
    "updateDateIncludingText": "2026-05-15T18:42:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations. (text: CR S2239)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-05-12T19:08:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4494is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4494\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Durbin (for himself, Mr. Blumenthal , Ms. Duckworth , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo prioritize funding for an expanded and sustained national investment in biomedical research.\n#### 1. Short title\nThis Act may be cited as the American Cures Act .\n#### 2. Appropriations for Innovation\n##### (a) In general\nThere are hereby authorized to be appropriated, and appropriated, out of any monies in the Treasury not otherwise appropriated, the following:\n**(1) National Institutes of Health**\nFor the National Institutes of Health at the Department of Health and Human Services\u2014\n**(A)**\nfor fiscal year 2027, $52,467,132,000;\n**(B)**\nfor fiscal year 2028, $56,507,101,164;\n**(C)**\nfor fiscal year 2029, $60,858,147,954;\n**(D)**\nfor fiscal year 2030, $65,544,225,346;\n**(E)**\nfor fiscal year 2031, $70,591,130,698;\n**(F)**\nfor fiscal year 2032, $76,026,647,762;\n**(G)**\nfor fiscal year 2033, $81,880,699,640;\n**(H)**\nfor fiscal year 2034, $88,185,513,512;\n**(I)**\nfor fiscal year 2035, $94,975,798,052;\n**(J)**\nfor fiscal year 2036, $102,288,934,502; and\n**(K)**\nfor fiscal year 2037 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(2) Centers for Disease Control and Prevention**\nFor the Centers for Disease Control and Prevention at the Department of Health and Human Services\u2014\n**(A)**\nfor fiscal year 2027,$ 9,911,621,307;\n**(B)**\nfor fiscal year 2028, $10,674,816,148;\n**(C)**\nfor fiscal year 2029, $11,496,776,991;\n**(D)**\nfor fiscal year 2030, $12,382,028,819;\n**(E)**\nfor fiscal year 2031, $13,335,445,038;\n**(F)**\nfor fiscal year 2032, $14,362,274,306;\n**(G)**\nfor fiscal year 2033, $15,468,169,428;\n**(H)**\nfor fiscal year 2034, $16,659,218,474;\n**(I)**\nfor fiscal year 2035, $17,941,978,296;\n**(J)**\nfor fiscal year 2036, $19,323,510,625; and\n**(K)**\nfor fiscal year 2037 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(3) Research, development, test, and evaluation program of the Department of Defense health program**\nFor the research, development, test, and evaluation program of the Department of Defense health program\u2014\n**(A)**\nfor fiscal year 2027, $2,939,358,093;\n**(B)**\nfor fiscal year 2028, $3,165,688,666;\n**(C)**\nfor fiscal year 2029, $3,409,451,694;\n**(D)**\nfor fiscal year 2030, $3,671,979,474;\n**(E)**\nfor fiscal year 2031, $3,954,721,894;\n**(F)**\nfor fiscal year 2032, $4,259,235,480;\n**(G)**\nfor fiscal year 2033, $4,587,196,612;\n**(H)**\nfor fiscal year 2034, $4,940,412,751;\n**(I)**\nfor fiscal year 2035, $5,320,824,534;\n**(J)**\nfor fiscal year 2036, $5,730,508,023; and\n**(K)**\nfor fiscal year 2037 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(4) Medical and prosthetics research program of the Department of Veterans Affairs**\nFor the medical and prosthetics research program of the Department of Veterans Affairs\u2014\n**(A)**\nfor fiscal year 2027, $1,071,765,000;\n**(B)**\nfor fiscal year 2028, $1,096,132,905;\n**(C)**\nfor fiscal year 2029, $1,180,535,138;\n**(D)**\nfor fiscal year 2030, $1,271,436,344;\n**(E)**\nfor fiscal year 2031, $1,369,336,942;\n**(F)**\nfor fiscal year 2032, $1,474,775,887;\n**(G)**\nfor fiscal year 2033, $1,588,333,630;\n**(H)**\nfor fiscal year 2034, $1,710,636,320;\n**(I)**\nfor fiscal year 2035, $1,842,355,321;\n**(J)**\nfor fiscal year 2036, $1,984,218,681; and\n**(K)**\nfor fiscal year 2037 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n##### (b) Availability\nAmounts appropriated under subsection (a) shall remain available until expended.\n##### (c) Definitions\nIn this section:\n**(1) Centers for Disease Control and Prevention**\nThe term Centers for Disease Control and Prevention means the appropriations accounts that support the various institutes, offices, and centers that make up the Centers for Disease Control and Prevention.\n**(2) Research, development, test, and evaluation program of the Department of Defense health program**\nThe term research, development, test, and evaluation program of the Department of Defense health program means the appropriations accounts that support the various institutes, offices, and centers that make up the research, development, test, and evaluation program of the Department of Defense health program.\n**(3) Medical and prosthetics research program of the Department of Veterans Affairs**\nThe term medical and prosthetics research program of the Department of Veterans Affairs means the appropriations accounts that support the various institutes, offices, and centers that make up the medical and prosthetics research program of the Department of Veterans Affairs.\n**(4) National Institutes of Health**\nThe term National Institutes of Health means the appropriations accounts that support the various institutes, offices, and centers that make up the National Institutes of Health.\n##### (d) Exemption of certain appropriations from sequestration\n**(1) In general**\nSection 255(g)(1)(A) of the Balanced Budget and Emergency Deficit Control Act ( 2 U.S.C. 905(g)(1)(A) ) is amended by inserting after Advances to the Unemployment Trust Fund and Other Funds (16\u20130327\u20130\u20131\u2013600). the following:\nAppropriations under the American Cures Act . .\n**(2) Applicability**\nThe amendment made by this section shall apply to any sequestration order issued under the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900 et seq. ) on or after the date of enactment of this Act.\n##### (e) Budgetary effects\n**(1) Statutory paygo scorecards**\nThe budgetary effects of this section shall not be entered on either PAYGO scorecard maintained pursuant to section 4(d) of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 933(d) ).\n**(2) Senate paygo scorecards**\nThe budgetary effects of this section shall not be entered on any PAYGO scorecard maintained for purposes of section 4106 of H. Con. Res. 71 (115th Congress).",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-15T18:34:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-05-12",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s4494",
          "measure-number": "4494",
          "measure-type": "s",
          "orig-publish-date": "2026-05-12",
          "originChamber": "SENATE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4494v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2026-05-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>American Cures Act </strong></p><p>This bill permanently funds several federal agencies and programs that perform biomedical research.</p><p>The bill provides specified funding for</p><ul><li>the National Institutes of Health,</li><li>the Centers for Disease Control and Prevention,</li><li>the Department of Defense health program, and</li><li>the Department of Veterans Affairs medical and prosthetics research program.</li></ul><p>The bill exempts the funding from sequestration, which is a process of automatic, usually across-the-board spending reductions under which budgetary resources are permanently cancelled to enforce specific budget policy goals.</p><p>It also exempts the budgetary effects of the funding from the Statutory Pay-As-You-Go (PAYGO) Act of 2010 and the Senate PAYGO rule.</p>"
        },
        "title": "American Cures Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4494.xml",
    "summary": {
      "actionDate": "2026-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Cures Act </strong></p><p>This bill permanently funds several federal agencies and programs that perform biomedical research.</p><p>The bill provides specified funding for</p><ul><li>the National Institutes of Health,</li><li>the Centers for Disease Control and Prevention,</li><li>the Department of Defense health program, and</li><li>the Department of Veterans Affairs medical and prosthetics research program.</li></ul><p>The bill exempts the funding from sequestration, which is a process of automatic, usually across-the-board spending reductions under which budgetary resources are permanently cancelled to enforce specific budget policy goals.</p><p>It also exempts the budgetary effects of the funding from the Statutory Pay-As-You-Go (PAYGO) Act of 2010 and the Senate PAYGO rule.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s4494"
    },
    "title": "American Cures Act"
  },
  "summaries": [
    {
      "actionDate": "2026-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Cures Act </strong></p><p>This bill permanently funds several federal agencies and programs that perform biomedical research.</p><p>The bill provides specified funding for</p><ul><li>the National Institutes of Health,</li><li>the Centers for Disease Control and Prevention,</li><li>the Department of Defense health program, and</li><li>the Department of Veterans Affairs medical and prosthetics research program.</li></ul><p>The bill exempts the funding from sequestration, which is a process of automatic, usually across-the-board spending reductions under which budgetary resources are permanently cancelled to enforce specific budget policy goals.</p><p>It also exempts the budgetary effects of the funding from the Statutory Pay-As-You-Go (PAYGO) Act of 2010 and the Senate PAYGO rule.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s4494"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4494is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "American Cures Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T02:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Cures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T02:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prioritize funding for an expanded and sustained national investment in biomedical research.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:31Z"
    }
  ]
}
```
