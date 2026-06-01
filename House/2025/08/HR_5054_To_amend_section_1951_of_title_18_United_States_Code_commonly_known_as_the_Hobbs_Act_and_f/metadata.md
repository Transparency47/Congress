# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5054
- Title: Freedom From Union Violence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5054
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2026-03-28T08:06:27Z
- Update date including text: 2026-03-28T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5054",
    "number": "5054",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Freedom From Union Violence Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:27Z",
    "updateDateIncludingText": "2026-03-28T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
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
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:00:05Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TN"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "LA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5054ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5054\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Perry (for himself, Mr. Ogles , Mr. Cloud , Mr. Crane , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 1951 of title 18, United States Code (commonly known as the Hobbs Act), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom From Union Violence Act of 2025 .\n#### 2. Interference with commerce by threats or violence\nSection 1951 of title 18, United States Code, is amended to read as follows:\n1951. Interference with commerce by threats or violence (a) Prohibition Except as provided in subsection (c), whoever in any way or degree obstructs, delays, or affects commerce or the movement of any article or commodity in commerce, by robbery or extortion, or attempts or conspires so to do, or commits or threatens physical violence to any person or property in furtherance of a plan or purpose to do anything in violation of this section, shall be fined not more than $100,000, imprisoned for a term of not more than 20 years, or both. (b) Definitions For purposes of this section\u2014 (1) the term commerce means any\u2014 (A) commerce within the District of Columbia, or any territory or possession of the United States; (B) commerce between any point in a State, territory, possession, or the District of Columbia and any point outside thereof; (C) commerce between points within the same State through any place outside that State; and (D) other commerce over which the United States has jurisdiction; (2) the term extortion means the obtaining of property from any person, with the consent of that person, if that consent is induced\u2014 (A) by actual or threatened use of force or violence, or fear thereof; (B) by wrongful use of fear not involving force or violence; or (C) under color of official right; (3) the term labor dispute has the same meaning as in section 2(9) of the National Labor Relations Act ( 29 U.S.C. 152(9) ); and (4) the term robbery means the unlawful taking or obtaining of personal property from the person or in the presence of another, against his or her will, by means of actual or threatened force or violence, or fear of injury, immediate or future\u2014 (A) to his or her person or property, or property in his or her custody or possession; or (B) to the person or property of a relative or member of his or her family, or of anyone in his or her company at the time of the taking or obtaining. (c) Exempted conduct (1) In general Subsection (a) does not apply to any conduct that\u2014 (A) is incidental to otherwise peaceful picketing during the course of a labor dispute; (B) consists solely of minor bodily injury, or minor damage to property, or threat or fear of such minor injury or damage; and (C) is not part of a pattern of violent conduct or of coordinated violent activity. (2) State and local jurisdiction Any violation of this section that involves any conduct described in paragraph (1) shall be subject to prosecution only by the appropriate State and local authorities. (d) Effect on other law Nothing in this section shall be construed\u2014 (1) to repeal, amend, or otherwise affect\u2014 (A) section 6 of the Clayton Act ( 15 U.S.C. 17 ); (B) section 20 of the Clayton Act ( 29 U.S.C. 52 ); (C) any provision of the Norris-LaGuardia Act ( 29 U.S.C. 101 et seq. ); (D) any provision of the National Labor Relations Act ( 29 U.S.C. 151 et seq. ); or (E) any provision of the Railway Labor Act ( 45 U.S.C. 151 et seq. ); or (2) to preclude Federal jurisdiction over any violation of this section, on the basis that the conduct at issue\u2014 (A) is also a violation of State or local law; or (B) occurred during the course of a labor dispute or in pursuit of a legitimate business or labor objective. .",
      "versionDate": "2025-08-26",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-26",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4154",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Employee Rights Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-19T15:52:34Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5054ih.xml"
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
      "title": "Freedom From Union Violence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-28T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom From Union Violence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-28T05:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 1951 of title 18, United States Code (commonly known as the Hobbs Act), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-28T05:31:53Z"
    }
  ]
}
```
