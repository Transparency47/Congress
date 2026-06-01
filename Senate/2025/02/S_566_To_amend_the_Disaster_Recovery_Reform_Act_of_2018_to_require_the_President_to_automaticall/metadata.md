# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/566?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/566
- Title: REPLACE Act
- Congress: 119
- Bill type: S
- Bill number: 566
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-05T21:46:52Z
- Update date including text: 2025-12-05T21:46:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/566",
    "number": "566",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "REPLACE Act",
    "type": "S",
    "updateDate": "2025-12-05T21:46:52Z",
    "updateDateIncludingText": "2025-12-05T21:46:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-13T17:31:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OK"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CO"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s566is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 566\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Hickenlooper (for himself, Mr. Lankford , Mr. Bennet , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Disaster Recovery Reform Act of 2018 to require the President to automatically waive certain critical document fees for individuals and households affected by major disasters for which assistance is provided under the Individuals and Households Program.\n#### 1. Short title\nThis Act may be cited as the Replacing Essential Passports and Licenses After Certain Emergencies Act or the REPLACE Act .\n#### 2. Critical document fee waiver\nSection 1238(a) of the Disaster Recovery Reform Act of 2018 ( 42 U.S.C. 5174b ) is amended\u2014\n**(1)**\nin paragraph (2), by striking applies regardless and inserting and the requirement of the President to waive fees under paragraph (4) apply regardless ;\n**(2)**\nby redesignating paragraph (4) as paragraph (8); and\n**(3)**\nby inserting after paragraph (3) the following:\n(4) Waiver The President, in consultation with the Governor of a State, shall provide a fee waiver described in paragraph (1) to any individual or household that has been adversely affected by a major disaster declared under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 )\u2014 (A) for which the President provides assistance to individuals and households under section 408 of that Act ( 42 U.S.C. 5174 ); and (B) that destroyed a critical document described in paragraph (1) of the individual or household. (5) Waiver availability The Secretary of State and the Director of the United States Citizenship and Immigration Services shall make publicly available on the website of the Department of State and the United States Citizenship and Immigration Services, respectively, a notice of the availability of fee waivers described in paragraph (4). (6) Report from USCIS Not later than 1 year after the date of enactment of this paragraph, and every year thereafter, the Director of the United States Citizenship and Immigration Services shall submit to Congress a report that includes, for the period covered by the report\u2014 (A) the number of fee waivers granted under this subsection; and (B) the cost to the United States Citizenship and Immigration Services of granting fee waivers under this subsection. (7) Report from Department of State Not later than 1 year after the date of enactment of this paragraph, and every year thereafter, the Secretary of State shall submit to Congress a report that includes, for the period covered by the report\u2014 (A) the number of fee waivers granted under this subsection; and (B) the cost to the Department of State of granting fee waivers under this subsection. .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-13",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "1338",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REPLACE Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-13T18:47:53Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s566is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "REPLACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REPLACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Replacing Essential Passports and Licenses After Certain Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Disaster Recovery Reform Act of 2018 to require the President to automatically waive certain critical document fees for individuals and households affected by major disasters for which assistance is provided under the Individuals and Households program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:01Z"
    }
  ]
}
```
