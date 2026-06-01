# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3146
- Title: HEROES Act
- Congress: 119
- Bill type: HR
- Bill number: 3146
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-04-21T08:05:55Z
- Update date including text: 2026-04-21T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3146",
    "number": "3146",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "HEROES Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:55Z",
    "updateDateIncludingText": "2026-04-21T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "LA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "OR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3146ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3146\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Goldman of New York (for himself and Mr. Fields ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to include service as a volunteer firefighter or volunteer emergency medical technician as a public service job for purposes of eligibility for the Public Service Loan Forgiveness Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Emergency Responders Overcome Student Debt Act or the HEROES Act .\n#### 2. Loan forgiveness for volunteer first responders\nSection 455(m)(3) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m)(3) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking or after the semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(iii) volunteer work as a qualified volunteer firefighter or qualified volunteer emergency medical technician in accordance with subparagraph (C). ; and\n**(2)**\nby adding at the end the following:\n(C) Qualified volunteer firefighter; qualified emergency medical technician (i) The term qualified volunteer firefighter means an individual who\u2014 (I) provides firefighting services, fire prevention services, emergency medical services, or other related emergency response services on behalf of a legally recognized fire department or public safety organization; and (II) is not otherwise directly employed on a full-time basis by the same fire department or public safety organization for which they provide such services. (ii) The term qualified volunteer emergency medical technician means an individual who\u2014 (I) is trained and certified, licensed, or otherwise authorized under applicable state or local laws to provide emergency medical care, pre-hospital care, or ambulance services in response to medical emergencies; (II) performs such care or services on behalf of an ambulance service, fire department, healthcare facility, or public safety organization; and (III) is not otherwise directly employed on a full-time basis by the same ambulance service, fire department, healthcare facility, or public safety organization for which they provide such care or services. (iii) The Secretary shall\u2014 (I) determine the minimum volunteer time required for a qualified volunteer firefighter or a qualified volunteer emergency medical technician to be treated as an individual employed in a full-time job for purposes of this subsection; and (II) ensure that such minimum volunteer time is not less than the amount of volunteer time that is required for the qualified volunteer firefighter or a qualified volunteer emergency medical technician to be considered an active member of the relevant ambulance service, fire department, healthcare facility, or public safety organization. (D) Public safety organization The term public safety organization means any State, local, or tribal governmental agency or nonprofit organization that has the principal purpose of protecting the safety of life, health, or property. .\n#### 3. Regulations\nThe Secretary of Education shall promulgate, after consultation with public safety organizations (which shall include firefighter and emergency responder organizations), regulations to carry out the amendments made by section 2, including regulations relating to\u2014\n**(1)**\nthe minimum volunteer time required for a qualified volunteer firefighter and qualified volunteer emergency medical technician to be treated as an individual employed in a full-time job for purposes of section 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ); and\n**(2)**\nthe process of tracking and verifying that volunteer time.",
      "versionDate": "2025-05-01",
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
        "name": "Education",
        "updateDate": "2025-06-04T13:46:08Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3146ih.xml"
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
      "title": "HEROES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEROES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Emergency Responders Overcome Student Debt Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to include service as a volunteer firefighter or volunteer emergency medical technician as a public service job for purposes of eligibility for the Public Service Loan Forgiveness Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:56Z"
    }
  ]
}
```
