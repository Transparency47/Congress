# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8179
- Title: FETCH Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8179
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-13T19:06:19Z
- Update date including text: 2026-04-13T19:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8179",
    "number": "8179",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "FETCH Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-13T19:06:19Z",
    "updateDateIncludingText": "2026-04-13T19:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:31:40Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NJ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MS"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8179ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8179\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Ms. Mace (for herself, Mr. Van Drew , Ms. Malliotakis , Mr. Ezell , and Mr. McCormick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize the use of funds under the Edward Byrne Memorial Justice Assistance Grant Program for police dog programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Enhancement for Tactical Canine Help Act of 2026 or the FETCH Act of 2026 .\n#### 2. Use of Byrne grants for K9 units\nSection 501(a)(1) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152(a)(1) ) is amended by adding at the end the following:\n(J) Police dog programs, including the following: (i) Acquiring police dogs. (ii) Training directly related to law enforcement duties involving police dogs, including on-duty general obedience training, and conditioning for the detection of narcotics, contraband, and explosives. (iii) Medications and dietary supplements for the wellness or service readiness of police dogs. (iv) Veterinary care for police dogs, including emergency services. (v) Insurance for veterinary, injury, death, replacement costs, or liability coverage related to police dogs. (vi) Dog food, including accommodations for special diets directly related to the service readiness or overall health of police dogs. (vii) Costs for equipment and supplies, including protective vests, identification collars, and first aid kits for police dogs. (viii) Costs related to housing needs for police dogs, including the creation or maintenance of kennels inside of a physical police department facility, or home-care stipends for law enforcement officers who care for police dogs at their home. (ix) Other costs related to routine care for police dogs. (x) Costs associated with police dogs after the dogs retire from service, including coverage for service-related injuries and chronic conditions, final veterinary care, formal adoption by the handling officer after the dog concludes its service, and the retrieval and delivery of administrative documents and certificates. .",
      "versionDate": "2026-04-02",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-13T19:06:19Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8179ih.xml"
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
      "title": "FETCH Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FETCH Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Enhancement for Tactical Canine Help Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize the use of funds under the Edward Byrne Memorial Justice Assistance Grant Program for police dog programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T05:18:32Z"
    }
  ]
}
```
