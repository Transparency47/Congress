# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/419?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/419
- Title: Protecting America From Spies Act
- Congress: 119
- Bill type: HR
- Bill number: 419
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-08-30T08:05:29Z
- Update date including text: 2025-08-30T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/419",
    "number": "419",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Protecting America From Spies Act",
    "type": "HR",
    "updateDate": "2025-08-30T08:05:29Z",
    "updateDateIncludingText": "2025-08-30T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "LA"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr419ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 419\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Cline (for himself, Mr. Bergman , Mr. Ogles , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 212 of the Immigration and Nationality Act to ensure that efforts to engage in espionage or technology transfer are considered in visa issuance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting America From Spies Act .\n#### 2. Expanding inadmissibility on security and related grounds\n##### (a) In general\nSection 212(a)(3)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(A) ) is amended to read as follows:\n(A) In general Any alien is inadmissible if a consular officer, an immigration officer, the Secretary of Homeland Security, or the Attorney General knows, or has reasonable ground to believe, that the alien\u2014 (i) engages, has engaged, or will engage in any activity\u2014 (I) in violation of any law of the United States relating to espionage or sabotage; or (II) that would violate any law of the United States relating to espionage or sabotage if the activity occurred in the United States; (ii) engages, has engaged, or will engage in any activity in violation or evasion of any law prohibiting the export from the United States of goods, technology, or sensitive information; (iii) seeks to enter the United States to engage solely, principally, or incidentally in any other unlawful activity; (iv) seeks to enter the United States to engage solely, principally, or incidentally in any activity a purpose of which is the opposition to, or the control or overthrow of, the Government of the United States by force, violence, or other unlawful means; or (v) is the spouse or child of an alien who is inadmissible under this subparagraph, if the activity causing the alien to be found inadmissible occurred within the last 5 years. .\n##### (b) Waiver authority\nSection 212(d)(3)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(3)(A) ) is amended by striking (other than paragraphs (3)(A)(i)(I), (3)(A)(ii), (3)(A)(iii), (3)(C), and clauses (i) and (ii) of paragraph (3)(E) of such subsection) each place such phrase appears and inserting (other than subparagraphs (A)(i)(I), (A)(ii), (A)(iii), (A)(iv), (C), (E)(i), and (E)(ii) of paragraph (3) of such subsection) .",
      "versionDate": "2025-01-15",
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
        "name": "Immigration",
        "updateDate": "2025-02-14T15:38:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr419",
          "measure-number": "419",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr419v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting America From Spies Act</strong></p><p>This bill expands the grounds for barring non-U.S. nationals (<em>aliens</em> under federal law) from entering the United States on the basis\u00a0of espionage or sabotage.</p><p>Currently, an individual is inadmissible if the individual seeks to enter the United States to engage in an act that (1) violates a U.S. law relating to espionage or sabotage; or (2) violates any U.S. law prohibiting the export of goods, technology, or sensitive information. Under the bill, an individual is inadmissible if the individual engages, has engaged, or will engage in such an act or in an act that would violate any U.S. law relating to espionage or sabotage if it occurred in the United States.</p><p>Furthermore, the bill expands these grounds of inadmissibility and other security-related grounds to cover the spouse or child of the barred individual if the act occurred in the last five years.</p>"
        },
        "title": "Protecting America From Spies Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr419.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting America From Spies Act</strong></p><p>This bill expands the grounds for barring non-U.S. nationals (<em>aliens</em> under federal law) from entering the United States on the basis\u00a0of espionage or sabotage.</p><p>Currently, an individual is inadmissible if the individual seeks to enter the United States to engage in an act that (1) violates a U.S. law relating to espionage or sabotage; or (2) violates any U.S. law prohibiting the export of goods, technology, or sensitive information. Under the bill, an individual is inadmissible if the individual engages, has engaged, or will engage in such an act or in an act that would violate any U.S. law relating to espionage or sabotage if it occurred in the United States.</p><p>Furthermore, the bill expands these grounds of inadmissibility and other security-related grounds to cover the spouse or child of the barred individual if the act occurred in the last five years.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr419"
    },
    "title": "Protecting America From Spies Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting America From Spies Act</strong></p><p>This bill expands the grounds for barring non-U.S. nationals (<em>aliens</em> under federal law) from entering the United States on the basis\u00a0of espionage or sabotage.</p><p>Currently, an individual is inadmissible if the individual seeks to enter the United States to engage in an act that (1) violates a U.S. law relating to espionage or sabotage; or (2) violates any U.S. law prohibiting the export of goods, technology, or sensitive information. Under the bill, an individual is inadmissible if the individual engages, has engaged, or will engage in such an act or in an act that would violate any U.S. law relating to espionage or sabotage if it occurred in the United States.</p><p>Furthermore, the bill expands these grounds of inadmissibility and other security-related grounds to cover the spouse or child of the barred individual if the act occurred in the last five years.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr419"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr419ih.xml"
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
      "title": "Protecting America From Spies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting America From Spies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 212 of the Immigration and Nationality Act to ensure that efforts to engage in espionage or technology transfer are considered in visa issuance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:23Z"
    }
  ]
}
```
