# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5755?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5755
- Title: No Budget, No Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 5755
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2026-04-15T08:06:07Z
- Update date including text: 2026-04-15T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5755",
    "number": "5755",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "No Budget, No Pay Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:06:07Z",
    "updateDateIncludingText": "2026-04-15T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-10-14T18:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "MI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5755ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5755\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Peters (for himself and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.\n#### 1. Short title\nThis Act may be cited as the No Budget, No Pay Act .\n#### 2. Definition\nIn this section, the term Member of Congress \u2014\n**(1)**\nhas the meaning given under section 2106 of title 5, United States Code; and\n**(2)**\ndoes not include the Vice President.\n#### 3. Timely approval of concurrent resolution on the budget and the appropriations bills\nIf both Houses of Congress have not approved a concurrent resolution on the budget as described under section 301 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 632 ) for a fiscal year before October 1 of that fiscal year and have not passed all the regular appropriations bills for the next fiscal year before October 1 of that fiscal year, the pay of each Member of Congress may not be paid for each day following that October 1 until the date on which both Houses of Congress approve a concurrent resolution on the budget for that fiscal year and all the regular appropriations bills.\n#### 4. No pay without concurrent resolution on the budget and the appropriations bills\n##### (a) In general\nNotwithstanding any other provision of law, no funds may be appropriated or otherwise be made available from the United States Treasury for the pay of any Member of Congress during any period determined by the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the Senate or the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the House of Representatives under section 5.\n##### (b) No retroactive pay\nA Member of Congress may not receive pay for any period determined by the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the Senate or the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the House of Representatives under section 5, at any time after the end of that period.\n#### 5. Determinations\n##### (a) Senate\n**(1) Request for certifications**\nOn October 1 of each year, the Secretary of the Senate shall submit a request to the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the Senate for certification of determinations made under paragraphs (2) (A) and (B).\n**(2) Determinations**\nThe Chairpersons of the Committee on the Budget and the Committee on Appropriations of the Senate shall\u2014\n**(A)**\non October 1 of each year, make a determination of whether Congress is in compliance with section 3 and whether Senators may not be paid under that section;\n**(B)**\ndetermine the period of days following each October 1 that Senators may not be paid under section 3; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Secretary of the Senate.\n##### (b) House of Representatives\n**(1) Request for certifications**\nOn October 1 of each year, the Chief Administrative Officer of the House of Representatives shall submit a request to the Chairpersons of the Committee on the Budget and the Committee on Appropriations of the House of Representatives for certification of determinations made under paragraphs (2) (A) and (B).\n**(2) Determinations**\nThe Chairpersons of the Committee on the Budget and the Committee on Appropriations of the House of Representatives shall\u2014\n**(A)**\non October 1 of each year, make a determination of whether Congress is in compliance with section 3 and whether Members of the House of Representatives may not be paid under that section;\n**(B)**\ndetermine the period of days following each October 1 that Members of the House of Representatives may not be paid under section 3; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Chief Administrative Officer of the House of Representatives.\n#### 6. Effective date\nThis section shall take effect on February 1, 2027.",
      "versionDate": "2025-10-14",
      "versionType": "Introduced in House"
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
        "name": "Congress",
        "updateDate": "2025-10-16T13:57:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-14",
    "originChamber": "House",
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
          "measure-id": "id119hr5755",
          "measure-number": "5755",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-14",
          "originChamber": "HOUSE",
          "update-date": "2025-10-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5755v00",
            "update-date": "2025-10-16"
          },
          "action-date": "2025-10-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.\u00a0</p>"
        },
        "title": "No Budget, No Pay Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5755.xml",
    "summary": {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.\u00a0</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5755"
    },
    "title": "No Budget, No Pay Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.\u00a0</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5755"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5755ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No Budget, No Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-15T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Budget, No Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-15T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-15T08:18:15Z"
    }
  ]
}
```
