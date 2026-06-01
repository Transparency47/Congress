# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6254?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6254
- Title: Medicaid Staffing Flexibility and Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6254
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2025-12-03T13:43:07Z
- Update date including text: 2025-12-03T13:43:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6254",
    "number": "6254",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Medicaid Staffing Flexibility and Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-03T13:43:07Z",
    "updateDateIncludingText": "2025-12-03T13:43:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:00:15Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "NC"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "NE"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6254ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6254\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Carter of Georgia (for himself, Mr. Davis of North Carolina , Mr. Dunn of Florida , Mr. Bacon , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to allow States more flexibility with respect to using contractors to make eligibility determinations and redeterminations and conduct fair hearings on behalf of the State Medicaid plan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medicaid Staffing Flexibility and Protection Act of 2025 .\n#### 2. State flexibility to use contractors to make eligibility determinations, redeterminations, and fair hearings on behalf of a state\n##### (a) Requirements With Respect to Eligibility Determinations\nSection 1902(a)(5) of the Social Security Act ( 42 U.S.C. 1396a(a)(5) ) is amended by inserting before the semicolon at the end the following: , but such determinations of eligibility may be made, at the option of a State, under a contract with another State or local agency or a contractor, so long as the contract does not provide incentives for the agency or contractor to delay eligibility determinations or to deny eligibility for individuals otherwise eligible for medical assistance .\n##### (b) Requirements With respect to fair hearings\nSection 1902(a)(3) of the Social Security Act ( 42 U.S.C. 1396a(a)(3) ) is amended by inserting before the semicolon at the end the following: , except that such fair hearing may be conducted, at the option of a State, under a contract with another State or local agency or a contractor, so long as such agency or contractor does not provide incentives to delay a fair hearing or to deny eligibility for an individual otherwise eligible for medical assistance .\n#### 3. Prohibiting conflicts of interest\nA State shall not use the flexibility provided under section 2 unless a contractor selected to conduct eligibility determinations or redeterminations pursuant to the amendments made by such section has no direct or indirect financial relationship with any Medicaid managed care organization (as defined in section 1903(m)(1)(A) of the Social Security Act ( 42 U.S.C. 1396b(m)(1)(A) )), including the network providers affiliated with such organization, that provides services to individuals entitled to medical assistance under title XIX of such Act ( 42 U.S.C. 1396 et seq. ) pursuant to a contract with such State.",
      "versionDate": "2025-11-21",
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
        "name": "Health",
        "updateDate": "2025-12-03T13:43:07Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6254ih.xml"
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
      "title": "Medicaid Staffing Flexibility and Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Staffing Flexibility and Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T11:08:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to allow States more flexibility with respect to using contractors to make eligibility determinations and redeterminations and conduct fair hearings on behalf of the State Medicaid plan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:23Z"
    }
  ]
}
```
