# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3601
- Title: National ACERT Grant Program Authorization Act
- Congress: 119
- Bill type: HR
- Bill number: 3601
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-02-10T09:05:34Z
- Update date including text: 2026-02-10T09:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3601",
    "number": "3601",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "National ACERT Grant Program Authorization Act",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:34Z",
    "updateDateIncludingText": "2026-02-10T09:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:01:35Z",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "FL"
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
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3601ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3601\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Pappas (for himself and Mr. Rutherford ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish the Adverse Childhood Experiences Response Team grant program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National ACERT Grant Program Authorization Act .\n#### 2. Adverse childhood experiences response team grant program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nOO Adverse childhood experiences response team grant program 3051. Grants for adverse childhood experiences response teams (a) Grants authorized From amounts made available to carry out this section, the Attorney General, in coordination with the Secretary of Health and Human Services, shall make grants to States, units of local government, Indian Tribes, and neighborhood or community-based organizations to address adverse childhood experiences associated with exposure to trauma. (b) Use of funds Amounts received under a grant under this section may be used to establish an adverse childhood experiences response team, including by\u2014 (1) establishing protocols to follow when encountering a child or youth exposed to trauma to facilitate access to services; (2) developing referral partnership agreements with behavioral health providers, substance treatment facilities, and recovery services for family members of children exposed to trauma; (3) integrating law enforcement, mental health, and crisis services to respond to situations where children have been exposed to trauma; (4) implementing comprehensive programs and practices to support children exposed to trauma; (5) identifying barriers for children to access trauma-informed care in their communities; (6) providing training in trauma-informed care to emergency response providers, victim service providers, child protective service professionals, educational institutions, and other community partners; (7) supporting cross-system planning and collaboration among officers and employees who work in law enforcement, court systems, child welfare services, correctional reentry programs, emergency medical services, health care services, public health, and substance abuse treatment and recovery support; and (8) providing technical assistance to communities, organizations, and public agencies on how to prevent and mitigate the impact of exposure to trauma and violence. (c) Application A State, unit of local government, Indian Tribe, or neighborhood or community-based organization desiring a grant under this section shall submit to the Attorney General an application in such form, and containing such information, as the Attorney General may reasonably require. (d) Authorization of appropriations To carry out this section, there is authorized to be appropriated $10,000,000 for each of the fiscal years 2026 through 2029. .",
      "versionDate": "2025-05-23",
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
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1897",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish the Adverse Childhood Experiences Response Team grant program, and for other purposes.",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-03T12:53:40Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3601ih.xml"
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
      "title": "National ACERT Grant Program Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National ACERT Grant Program Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish the Adverse Childhood Experiences Response Team grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:33Z"
    }
  ]
}
```
