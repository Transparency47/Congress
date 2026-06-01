# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4073?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4073
- Title: Transportation Security Administration Pay Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4073
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-05-29T16:52:41Z
- Update date including text: 2026-05-29T16:52:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4073",
    "number": "4073",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Transportation Security Administration Pay Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T16:52:41Z",
    "updateDateIncludingText": "2026-05-29T16:52:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T17:18:03Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NM"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "RI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "CT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-21",
      "state": "IL"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4073is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4073\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Ms. Rosen (for herself and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for essential Transportation Security Administration pay and operations during the lapse in appropriations beginning on February 14, 2026, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transportation Security Administration Pay Act of 2026 .\n#### 2. Continuing appropriations for Transportation Security Administration personnel\n##### (a) In general\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for the period beginning on February 14, 2026, during which interim or full-year appropriations for fiscal year 2026 are not in effect, such sums as are necessary to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to employees of the Transportation Security Administration.\n##### (b) Limitation to individuals affected by lapse in appropriations\nAmounts provided under subsection (a) may not be used to provide pay, allowances, pay differentials, benefits, or other payments to an employee of the Transportation Security Administration for any portion of the period described in subsection (a) for which the employee is provided with such pay, allowances, pay differentials, benefits, or other payments using amounts other than amounts provided under subsection (a).\n##### (c) Charge to future appropriations\nExpenditures made pursuant to subsection (a) shall be charged to the applicable appropriation, fund, or authorization whenever an Act in which such applicable appropriation, fund, or authorization is included is enacted into law.\n##### (d) Terms and conditions\nPay, allowances, pay differentials, benefits, and other payments provided by the Transportation Security Administration using amounts provided under subsection (a) shall be subject to the requirements, authorities, conditions, and limitations applicable with respect to the provision of pay, allowances, pay differentials, benefits, and other payments by the Transportation Security Administration under the Full-Year Continuing Appropriations and Extensions Act, 2025 ( Public Law 119\u20134 ; 139 Stat. 9).\n#### 3. Termination\nAppropriations and funds made available and authority granted under section 2 shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nSeptember 30, 2026.\n#### 4. Retroactive effective date\nThis Act shall take effect as if enacted on February 13, 2026.",
      "versionDate": "2026-03-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-28",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WATCH Personnel Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-18",
        "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 362."
      },
      "number": "4127",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Transportation Security Administration Pay Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-19",
        "text": "Referred to the Committee on Appropriations, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8902",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WATCH Personnel Act of 2026",
      "type": "HR"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-19T12:56:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-12",
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
          "measure-id": "id119s4073",
          "measure-number": "4073",
          "measure-type": "s",
          "orig-publish-date": "2026-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4073v00",
            "update-date": "2026-03-19"
          },
          "action-date": "2026-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Transportation Security Administration Pay Act of 2026</strong></p><p>This bill provides continuing appropriations to provide pay and benefits to Transportation Security Administration (TSA) employees during the partial Department of Homeland Security (DHS) shutdown that began on February 14, 2026. (A partial government shutdown is currently in effect for\u00a0TSA and other DHS\u00a0agencies because the FY2026 DHS appropriations bill has not been enacted and continuing appropriations for DHS are not in effect.)</p><p>Specifically, the bill provides FY2026 continuing appropriations to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to\u00a0TSA employees during the period in which interim or full-year FY2026 appropriations are not in effect.</p><p>The bill provides the continuing appropriations until the earlier of (1) the enactment into law of the applicable appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill must take effect as if it had been enacted on February 13, 2026.</p>"
        },
        "title": "Transportation Security Administration Pay Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4073.xml",
    "summary": {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transportation Security Administration Pay Act of 2026</strong></p><p>This bill provides continuing appropriations to provide pay and benefits to Transportation Security Administration (TSA) employees during the partial Department of Homeland Security (DHS) shutdown that began on February 14, 2026. (A partial government shutdown is currently in effect for\u00a0TSA and other DHS\u00a0agencies because the FY2026 DHS appropriations bill has not been enacted and continuing appropriations for DHS are not in effect.)</p><p>Specifically, the bill provides FY2026 continuing appropriations to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to\u00a0TSA employees during the period in which interim or full-year FY2026 appropriations are not in effect.</p><p>The bill provides the continuing appropriations until the earlier of (1) the enactment into law of the applicable appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill must take effect as if it had been enacted on February 13, 2026.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s4073"
    },
    "title": "Transportation Security Administration Pay Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transportation Security Administration Pay Act of 2026</strong></p><p>This bill provides continuing appropriations to provide pay and benefits to Transportation Security Administration (TSA) employees during the partial Department of Homeland Security (DHS) shutdown that began on February 14, 2026. (A partial government shutdown is currently in effect for\u00a0TSA and other DHS\u00a0agencies because the FY2026 DHS appropriations bill has not been enacted and continuing appropriations for DHS are not in effect.)</p><p>Specifically, the bill provides FY2026 continuing appropriations to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to\u00a0TSA employees during the period in which interim or full-year FY2026 appropriations are not in effect.</p><p>The bill provides the continuing appropriations until the earlier of (1) the enactment into law of the applicable appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill must take effect as if it had been enacted on February 13, 2026.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s4073"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4073is.xml"
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
      "title": "Transportation Security Administration Pay Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transportation Security Administration Pay Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for essential Transportation Security Administration pay and operations during the lapse in appropriations beginning on February 14, 2026, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:30Z"
    }
  ]
}
```
