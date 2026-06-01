# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6453
- Title: ADA 30 Days to Comply Act
- Congress: 119
- Bill type: HR
- Bill number: 6453
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-18T15:28:55Z
- Update date including text: 2026-05-18T15:28:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 8.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 8.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6453",
    "number": "6453",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "ADA 30 Days to Comply Act",
    "type": "HR",
    "updateDate": "2026-05-18T15:28:55Z",
    "updateDateIncludingText": "2026-05-18T15:28:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 8.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
        "item": [
          {
            "date": "2026-03-26T18:29:46Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-04T14:06:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6453ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6453\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Lawler (for himself and Mr. Correa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Americans with Disabilities Act of 1990 to provide for a remediation period before the commencement of a civil action.\n#### 1. Short title\nThis Act may be cited as the ADA 30 Days to Comply Act .\n#### 2. Notice and cure period\nParagraph (1) of section 308(a) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12188(a)(1) ) is amended to read as follows:\n(1) Availability of remedies and procedures (A) In general Subject to subparagraph (B), the remedies and procedures set forth in section 204(a) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a\u20133(a) ) are the remedies and procedures this title provides to any person who is being subjected to discrimination on the basis of disability in violation of this title or who has reasonable grounds for believing that such person is about to be subjected to discrimination in violation of section 303. Nothing in this section shall require a person with a disability to engage in a futile gesture if such person has actual notice that a person or organization covered by this title does not intend to comply with its provisions. (B) Barriers to access to existing public accommodations A civil action under section 302 or 303 based on the failure to remove an architectural barrier to access into an existing public accommodation may not be commenced by a person aggrieved by such failure unless\u2014 (i) that person has provided to the owner or operator of the accommodation a written notice specific enough to allow such owner or operator to identify the barrier; and (ii) (I) during the period beginning on the date the notice is received and ending 30 days after that date, the owner or operator fails to provide to that person a written description outlining improvements that will be made to remove the barrier; or (II) if the owner or operator provides the written description under subclause (I), the owner or operator fails to remove the barrier or, in the case of a barrier, the removal of which requires additional time as a result of circumstances beyond the control of the owner or operator, fails to make substantial progress in removing the barrier during the period beginning on the date the description is provided and ending 30 days after that date. (C) Specification of details of alleged violation The written notice required under subparagraph (B) must also specify in detail the circumstances under which an individual was actually denied access to a public accommodation, including the address of property, whether a request for assistance in removing an architectural barrier to access was made, and whether the barrier to access was a permanent or temporary barrier. (D) Notice specific enough For purposes of this paragraph, the term notice specific enough means notice that allows such owner or operator to identify the barrier to access in question. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2026-04-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8396",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACCESS Act of 2026.",
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
            "name": "Architecture",
            "updateDate": "2026-05-18T15:28:54Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-05-18T15:28:45Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2026-05-18T15:28:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-01-06T15:28:55Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6453ih.xml"
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
      "title": "ADA 30 Days to Comply Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ADA 30 Days to Comply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Americans with Disabilities Act of 1990 to provide for a remediation period before the commencement of a civil action.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T03:48:17Z"
    }
  ]
}
```
