# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6817
- Title: Home-Based Telemental Health Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6817
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-12T08:05:53Z
- Update date including text: 2026-05-12T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6817",
    "number": "6817",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Home-Based Telemental Health Care Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:53Z",
    "updateDateIncludingText": "2026-05-12T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6817ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6817\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Salinas (for herself and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a home-based telemental health care grant program for purposes of increasing mental health and substance use services in rural medically underserved populations and for individuals in farming, fishing, and forestry occupations.\n#### 1. Short title\nThis Act may be cited as the Home-Based Telemental Health Care Act of 2025 .\n#### 2. Mental health and substance use services delivered to rural underserved populations via telemental health care\nTitle III of the Public Health Service Act is amended by inserting after section 330K ( 42 U.S.C. 254c\u201316 ) the following:\n330K\u20131. Mental health and substance use services delivered to rural underserved populations via telemental health care (a) Definitions In this section\u2014 (1) the term covered populations means\u2014 (A) health professional shortage areas (as defined in section 332(a)(1)) in rural areas; or (B) populations engaged in a farming, fishing, or forestry industry; (2) the term eligible entity means a public or nonprofit private telemental health provider network that offers services that include mental health and substance use services provided by professionals trained in mental health and substance use; (3) the term farming, fishing, or forestry industry means an occupation defined as a farming, fishing, or forestry occupation by the Department of Labor in accordance with the Standard Occupational Classification System; (4) the term home-based telemental means the use of telemental health services where the patient is in his or her own home or other place of comfort; (5) the term professional trained in mental health means a psychiatrist, a qualified mental health professional (as defined in section 330K), or another mental health professional acting under the direction of a psychiatrist; (6) the term rural has the meaning given such term by the Office of Rural Health Policy of the Health Resources and Services Administration; and (7) the term telemental health means the use of electronic information and telecommunications technologies to support long distance clinical health care, patient and professional health-related education, public health, and health administration. (b) Program authorized The Secretary, in consultation with the Rural Health Liaison of the Department of Agriculture, shall award grants to eligible entities to expand and enhance access to mental health and substance use services for covered populations in their homes or other places of comfort, as delivered remotely by professionals trained in mental health and substance use using telemental health care. (c) Use of funds Recipients of a grant under this section shall use the grant funds to\u2014 (1) deliver home-based telemental health services to covered populations; (2) develop comprehensive metrics to measure the quality and impact of home-based telemental health services compared to traditional in-person mental health and substance use care; and (3) support infrastructure that enhances the capacity of health care providers to deliver telemental health services in patients\u2019 homes or other places of comfort, including by\u2014 (A) expanding broadband access; (B) providing devices for patients to access telemental health services; and (C) offsetting costs of technology necessary for health care providers to deliver high quality care. (d) Report The Secretary, in consultation with the Secretary of Agriculture, not later than 3 years after the date on which the program under this section commences, and 2 years thereafter, shall submit to the appropriate congressional committees reports on the impact and quality of care of home-based telemental health care services for covered populations. (e) Authorized use of funds Out of any amounts made available to the Secretary, up to $10,000,000 for each of fiscal years 2025 through 2029 may be allocated to carrying out the program under this section. .",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1056",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Home-Based Telemental Health Care Act of 2025",
      "type": "S"
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
        "updateDate": "2026-01-15T13:23:07Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6817ih.xml"
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
      "title": "Home-Based Telemental Health Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home-Based Telemental Health Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a home-based telemental health care grant program for purposes of increasing mental health and substance use services in rural medically underserved populations and for individuals in farming, fishing, and forestry occupations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T03:18:17Z"
    }
  ]
}
```
