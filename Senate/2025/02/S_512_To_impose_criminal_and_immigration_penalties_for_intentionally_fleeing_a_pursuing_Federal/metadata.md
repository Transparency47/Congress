# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/512?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/512
- Title: Agent Raul Gonzalez Officer Safety Act
- Congress: 119
- Bill type: S
- Bill number: 512
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-11-30T06:40:39Z
- Update date including text: 2025-11-30T06:40:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/512",
    "number": "512",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Agent Raul Gonzalez Officer Safety Act",
    "type": "S",
    "updateDate": "2025-11-30T06:40:39Z",
    "updateDateIncludingText": "2025-11-30T06:40:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T17:07:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ND"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "OK"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s512is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 512\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Cruz (for himself, Mr. Sheehy , Mr. Cassidy , Mrs. Britt , Mr. Cramer , Mr. Justice , Mr. Budd , Mrs. Hyde-Smith , Mr. Lankford , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo impose criminal and immigration penalties for intentionally fleeing a pursuing Federal officer while operating a motor vehicle.\n#### 1. Short title\nThis Act may be cited as Agent Raul Gonzalez Officer Safety Act .\n#### 2. Criminal penalties for evading arrest or detention\n##### (a) In general\nChapter 2 of title 18, United States Code, is amended by adding at the end the following:\n40B. Evading arrest or detention while operating a motor vehicle (a) Offense A person commits an offense under this section by operating a motor vehicle within 100 miles of the United States border while intentionally fleeing from\u2014 (1) a pursuing U.S. Border Patrol agent acting pursuant to lawful authority; or (2) any pursuing Federal, State, or local law enforcement officer who is actively assisting, or under the command of, U.S. Border Patrol. (b) Penalties (1) In general Except as provided in paragraphs (2) and (3), any person who commits an offense described in subsection (a) shall be\u2014 (A) imprisoned for a term of not more than 2 years; (B) fined under this title; or (C) subject to the penalties described in subparagraphs (A) and (B). (2) Serious bodily injury If serious bodily injury results from the commission of an offense described in subsection (a), the person committing such offense shall be\u2014 (A) imprisoned for a term of not less than 5 years and not more than 20 years; (B) fined under this title; or (C) subject to the penalties described in subparagraphs (A) and (B). (3) Death If the death of any person results from the commission of an offense described in subsection (a), the person committing such offense shall be\u2014 (A) imprisoned for a term of not less than 10 years and up to life; (B) fined under this title; or (C) subject to the penalties described in subparagraphs (A) and (B). .\n##### (b) Clerical amendment\nThe analysis for chapter 2 of title 18, United States Code, is amended by adding at the end the following:\n40B. Evading arrest or detention while operating a motor vehicle. .\n#### 3. Inadmissibility, deportability, and ineligibility related to evading arrest or detention while operating a motor vehicle\n##### (a) Inadmissibility\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) is amended by adding at the end the following:\n(J) Evading arrest or detention while operating a motor vehicle Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, a violation of section 40B(a) of title 18, United States Code, is inadmissible. .\n##### (b) Deportability\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Evading arrest or detention while operating a motor vehicle Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, a violation of section 40B(a) of title 18, United States Code, is deportable. .\n##### (c) Ineligibility for relief\nSection 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ) is amended by adding at the end the following:\n(f) Ineligibility for relief as a result of evading arrest or detention while operating a motor vehicle Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, a violation of section 40B(a) of title 18, United States Code, shall be ineligible for relief under the immigration laws, including asylum under this section. .\n#### 4. Annual report\nThe Attorney General, in consultation with the Secretary of Homeland Security, shall submit an annual report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives that\u2014\n**(1)**\nidentifies the number of people who committed a violation of section 40B(a) of title 18, United States Code, as added by section 2(a); and\n**(2)**\nsummarizes\u2014\n**(A)**\nthe number of individuals who were charged with such violation;\n**(B)**\nthe number of individuals who were apprehended for, but not charged with, such violation;\n**(C)**\nthe number of individuals who committed such violation, but were not apprehended;\n**(D)**\nthe penalties sought in the charging documents pertaining to such violation; and\n**(E)**\nthe penalties imposed for such violation.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-13",
        "text": "Received in the Senate and Read twice and referred to the Committee on the Judiciary."
      },
      "number": "35",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Agent Raul Gonzalez Officer Safety Act",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-05-02T14:55:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-02T14:55:42Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-05-02T14:55:42Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-05-02T14:55:42Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-05-02T14:55:42Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-05-02T14:55:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-13T15:15:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s512",
          "measure-number": "512",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s512v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Agent Raul Gonzalez Officer Safety Act</strong></p><p>This bill establishes new federal criminal offenses for operating a motor vehicle within 100 miles of the U.S. border while fleeing from a U.S. Border Patrol agent or a federal, state, or local law enforcement officer who is actively assisting or under the command of the U.S. Border Patrol.</p><p>The bill establishes criminal penalties for an offense, including a mandatory minimum prison term for an offense resulting in death or serious bodily injury. Additionally, a non-U.S. national who is convicted of or admits to committing an offense is inadmissible, deportable, and ineligible\u00a0for immigration relief (including asylum).</p>"
        },
        "title": "Agent Raul Gonzalez Officer Safety Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s512.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Agent Raul Gonzalez Officer Safety Act</strong></p><p>This bill establishes new federal criminal offenses for operating a motor vehicle within 100 miles of the U.S. border while fleeing from a U.S. Border Patrol agent or a federal, state, or local law enforcement officer who is actively assisting or under the command of the U.S. Border Patrol.</p><p>The bill establishes criminal penalties for an offense, including a mandatory minimum prison term for an offense resulting in death or serious bodily injury. Additionally, a non-U.S. national who is convicted of or admits to committing an offense is inadmissible, deportable, and ineligible\u00a0for immigration relief (including asylum).</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s512"
    },
    "title": "Agent Raul Gonzalez Officer Safety Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Agent Raul Gonzalez Officer Safety Act</strong></p><p>This bill establishes new federal criminal offenses for operating a motor vehicle within 100 miles of the U.S. border while fleeing from a U.S. Border Patrol agent or a federal, state, or local law enforcement officer who is actively assisting or under the command of the U.S. Border Patrol.</p><p>The bill establishes criminal penalties for an offense, including a mandatory minimum prison term for an offense resulting in death or serious bodily injury. Additionally, a non-U.S. national who is convicted of or admits to committing an offense is inadmissible, deportable, and ineligible\u00a0for immigration relief (including asylum).</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s512"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s512is.xml"
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
      "title": "Agent Raul Gonzalez Officer Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Agent Raul Gonzalez Officer Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose criminal and immigration penalties for intentionally fleeing a pursuing Federal officer while operating a motor vehicle.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:34Z"
    }
  ]
}
```
