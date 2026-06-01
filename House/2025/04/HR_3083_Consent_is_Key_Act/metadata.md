# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3083?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3083
- Title: Consent is Key Act
- Congress: 119
- Bill type: HR
- Bill number: 3083
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-07-11T08:05:58Z
- Update date including text: 2025-07-11T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3083",
    "number": "3083",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Consent is Key Act",
    "type": "HR",
    "updateDate": "2025-07-11T08:05:58Z",
    "updateDateIncludingText": "2025-07-11T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:02:15Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DC"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3083ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3083\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mrs. Torres of California (for herself, Ms. Stansbury , Ms. Norton , Mr. Larson of Connecticut , Ms. Clarke of New York , Ms. Schakowsky , Ms. Tlaib , and Mrs. Cherfilus-McCormick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo encourage States to voluntarily pass laws to authorize civil damages and equitable relief for nonconsensual sexual protection barrier removal, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Consent is Key Act .\n#### 2. Increased funding for formula grants authorized\nThe Attorney General shall increase the amount provided to a State under the covered formula grant if the State has in effect a law that authorizes a civil action, for damages and such equitable relief as may be appropriate, against a person who engages in nonconsensual sexual protection barrier removal.\n#### 3. Application\nA State seeking an increase in the amount provided to the State under the covered formula grant shall include in the application of the State for each covered formula grant such information as the Attorney General may reasonably require, including information about the law described in section 2.\n#### 4. Grant increase\nThe amount of the increase provided to a State under the covered formula grant shall be equal to not more than 20 percent of the average of the total amount of funding provided to the State under the covered formula grant under the 3 most recent awards to the State.\n#### 5. Period of increase\n##### (a) In general\nThe Attorney General shall provide an increase in the amount provided to a State under the covered formula grant for a 4-year period.\n##### (b) Limit\nThe Attorney General may not provide an increase in the amount provided to a State under the covered formula grant more than 4 times.\n#### 6. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $5,000,000 for each of fiscal years 2026 through 2030.\n#### 7. Definitions\nIn this Act:\n**(1) Covered formula grant**\nThe term covered formula grant means a grant under section 41601 of the Violence Against Women Act of 1994 ( 34 U.S.C. 12511 et seq. ) (commonly referred to as the Sexual Assault Services Program ).\n**(2) Nonconsensual sexual protection barrier removal**\nThe term nonconsensual sexual protection barrier removal means removal of a sexual protection barrier from a body part, including the genitals, or an object being used by a person for sexual contact with another person without the consent of each person involved in such sexual contact, causing sexual contact between the body parts, including the genitals, or objects being used for sexual contact, and the body of any person engaged in such sexual contact.\n**(3) Sexual protection barrier**\nThe term sexual protection barrier may include a condom, including an internal condom, a dental dam, or any other barrier against sexual fluids during sexual contact.",
      "versionDate": "2025-04-29",
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
        "name": "Law",
        "updateDate": "2025-05-21T12:41:18Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3083ih.xml"
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
      "title": "Consent is Key Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Consent is Key Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To encourage States to voluntarily pass laws to authorize civil damages and equitable relief for nonconsensual sexual protection barrier removal, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:33Z"
    }
  ]
}
```
