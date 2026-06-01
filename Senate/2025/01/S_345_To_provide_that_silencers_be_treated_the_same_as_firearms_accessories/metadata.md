# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/345
- Title: SHUSH Act
- Congress: 119
- Bill type: S
- Bill number: 345
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-02-12T12:03:23Z
- Update date including text: 2026-02-12T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/345",
    "number": "345",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SHUSH Act",
    "type": "S",
    "updateDate": "2026-02-12T12:03:23Z",
    "updateDateIncludingText": "2026-02-12T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
        "item": [
          {
            "date": "2025-01-30T22:22:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-30T22:22:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "NE"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "UT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "LA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s345is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 345\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Lee (for himself, Mr. Scott of Florida , Mr. Ricketts , Mr. Curtis , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide that silencers be treated the same as firearms accessories.\n#### 1. Short title\nThis Act may be cited as the Silencers Help Us Save Hearing Act or the SHUSH Act .\n#### 2. Equal treatment of silencers and firearms\n##### (a) In general\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking (7) any silencer and all that follows through ; and (8) and inserting and (7) .\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of enactment of this Act.\n**(2) Transfers**\nIn the case of the tax imposed by section 5811 of the Internal Revenue Code of 1986, the amendments made by this section shall apply with respect to transfers after the date which is 2 years prior to the date of enactment of this Act.\n#### 3. Treatment of certain silencers\nSection 5841 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(f) Firearm silencers A person acquiring or possessing a firearm silencer in accordance with chapter 44 of title 18, United States Code, shall be treated as meeting any registration and licensing requirements of the National Firearms Act (as in effect on the day before the date of the enactment of this subsection) with respect to such silencer. .\n#### 4. Preemption of certain State laws in relation to firearm silencers\nSection 927 of title 18, United States Code, is amended by adding at the end the following: Notwithstanding the preceding sentence, a law of a State or a political subdivision of a State that, as a condition of lawfully making, transferring, using, possessing, or transporting a firearm silencer in interstate or foreign commerce, imposes a tax on any such conduct, or a marking, recordkeeping, or registration requirement with respect to the firearm silencer, shall have no force or effect. .\n#### 5. Silencers and mufflers not to be federally regulated\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by striking (C) any firearm muffler or firearm silencer; or (D) and inserting or (C) ; and\n**(2)**\nby striking paragraph (25).\n##### (b) Penalties\nSection 924 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (B)(ii), by striking \u2018\u2018, or is equipped with a firearm silencer or firearm muffler\u2019\u2019; and\n**(B)**\nin subparagraph (C)(ii), by striking \u2018\u2018or is equipped with a firearm silencer or firearm muffler,\u2019\u2019; and\n**(2)**\nin subsection (o), by striking or is equipped with a firearm silencer or muffler, .\n##### (c) Carrying of concealed firearms by qualified law enforcement officers\nSection 926B(e)(3) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by adding and at the end;\n**(2)**\nby striking subparagraph (B); and\n**(3)**\nby redesignating subparagraph (C) as subparagraph (B).\n##### (d) Carrying of concealed firearms by qualified retired law enforcement officers\nSection 926C(e)(1)(C) of title 18, United States Code, is amended\u2014\n**(1)**\nin clause (i), by adding and at the end;\n**(2)**\nby striking clause (ii); and\n**(3)**\nby redesignating clause (iii) as clause (ii).\n#### 6. Excepting silencers from regulation by the Consumer Product Safety Commission\nSection 3(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ) is amended\u2014\n**(1)**\nin subparagraph (H), by striking or at the end;\n**(2)**\nin subparagraph (I), by striking Act). and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(J) any firearm muffler or firearm silencer (as such term is defined in section 5841(f) of the Internal Revenue Code of 1986). .",
      "versionDate": "2025-01-30",
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
        "actionDate": "2025-01-31",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "850",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHUSH Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-04T20:13:24Z"
          },
          {
            "name": "Consumer Product Safety Commission",
            "updateDate": "2025-04-04T20:13:30Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-04-04T20:13:08Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-04-04T20:13:46Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-04-04T20:13:02Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-04T20:12:58Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-04-04T20:13:17Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-04T20:13:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-07T15:57:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s345",
          "measure-number": "345",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-12-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s345v00",
            "update-date": "2025-12-04"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation\u00a0under federal firearms laws.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Additionally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul><p>Finally, the bill excludes firearm mufflers and silencers from<em></em> regulation by the Consumer Product Safety Commission.\u00a0(Current law generally excludes firearms from regulation by the commission.)</p>"
        },
        "title": "SHUSH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s345.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation\u00a0under federal firearms laws.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Additionally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul><p>Finally, the bill excludes firearm mufflers and silencers from<em></em> regulation by the Consumer Product Safety Commission.\u00a0(Current law generally excludes firearms from regulation by the commission.)</p>",
      "updateDate": "2025-12-04",
      "versionCode": "id119s345"
    },
    "title": "SHUSH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation\u00a0under federal firearms laws.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Additionally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul><p>Finally, the bill excludes firearm mufflers and silencers from<em></em> regulation by the Consumer Product Safety Commission.\u00a0(Current law generally excludes firearms from regulation by the commission.)</p>",
      "updateDate": "2025-12-04",
      "versionCode": "id119s345"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s345is.xml"
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
      "title": "SHUSH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHUSH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Silencers Help Us Save Hearing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that silencers be treated the same as firearms accessories.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:25Z"
    }
  ]
}
```
