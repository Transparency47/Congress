# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3547
- Title: Servicemember Healthcare Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3547
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-03-19T08:07:12Z
- Update date including text: 2026-03-19T08:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3547",
    "number": "3547",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Servicemember Healthcare Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:12Z",
    "updateDateIncludingText": "2026-03-19T08:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NH"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AZ"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3547ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3547\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mrs. Kiggans of Virginia (for herself and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to allow members of the Selected Reserve and National Guard holding employment within the Federal Government the choice between military and civilian healthcare plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember Healthcare Freedom Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThousands of members of reserve components and the National Guard, in addition to their military service, work for the United States Government in a civilian capacity.\n**(2)**\nNearly all members of the Selected Reserve and the National Guard, and their families, are entitled to purchase a TRICARE Reserve Select (TRS) healthcare plan as a service-related benefit.\n**(3)**\nAs of the day before the date of the enactment of this Act, eligibility for Federal Employee Health Benefits (FEHB) prohibits members of the Selected Reserve and National Guard from enrolling in Tricare Reserve Select plans.\n**(4)**\nRemoval of such prohibition for members of the Selected Reserve and the National Guard will provide continuity of care throughout mobilization cycles.\n**(5)**\nProviding members of the Armed Forces with the ability to purchase comprehensive, low-cost health insurance increases the readiness and lethality of the Armed Forces as a whole.\n#### 3. Modification of expiration date to allow members of the Selected Reserve and National Guard, eligible for Federal Employee Health Benefits, to enroll into TRICARE Reserve Select as of January 1, 2026\nSection 1076d(a)(2) of title 10, United States Code, is amended by striking January 1, 2030 and inserting January 1, 2026 .",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "1861",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Servicemember Healthcare Freedom Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:38:07Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3547ih.xml"
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
      "title": "Servicemember Healthcare Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T06:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemember Healthcare Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to allow members of the Selected Reserve and National Guard holding employment within the Federal Government the choice between military and civilian healthcare plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T06:48:32Z"
    }
  ]
}
```
