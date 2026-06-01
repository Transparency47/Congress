# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2372
- Title: DEVICE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2372
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-04-07T13:05:58Z
- Update date including text: 2025-04-07T13:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2372",
    "number": "2372",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "DEVICE Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-07T13:05:58Z",
    "updateDateIncludingText": "2025-04-07T13:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:02:05Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-26",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2372ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2372\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Lieu (for himself, Ms. Chu , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to enhance medical device communications and ensure device cleanliness.\n#### 1. Short title\nThis Act may be cited as the Disclosure; and Encouragement of Verification, Innovation, Cleaning, and Efficiency Act of 2025 or the DEVICE Act of 2025 .\n#### 2. Reporting requirement for design and reprocessing instruction changes\n##### (a) Adulteration\nSection 501 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 ) is amended by inserting after paragraph (j) the following:\n(k) If it is a device with respect to which the manufacturer is in violation of the reporting requirement under section 510(r) (relating to design and reprocessing changes). .\n##### (b) Requirement\nSection 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ) is amended by adding at the end the following:\n(r) Reporting requirement for device design changes Before making a change to the design of a device, or the reprocessing instructions of a device, that is marketed in interstate commerce, the manufacturer of the device shall give written notice of the change to the Secretary. .\n#### 3. Reporting requirement for certain communications to foreign health care providers\n##### (a) Adulteration\nSection 501 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 ), as amended by section 2 of this Act, is further amended by inserting after paragraph (k) the following:\n(l) If it is a device with respect to which the manufacturer is in violation of the reporting requirement under section 510(s) (relating to communications to foreign health care providers). .\n##### (b) Requirement\nSection 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ), as amended by section 2 of this Act, is further amended by adding at the end the following:\n(s) Reporting requirement for certain communications to foreign health care providers (1) Requirement The manufacturer of a device that is marketed in interstate commerce shall give written notice to the Secretary of any communication described in paragraph (2) not more than 5 calendar days after making such communication. (2) Communication described A communication is described in this paragraph if the communication\u2014 (A) is made by the manufacturer of the device or an affiliate of the manufacturer; (B) relates to a change to the design of the device, a change to the recommended reprocessing protocols, if any, for the device, or a safety concern about the device; and (C) is widely disseminated (including on a voluntary basis) to health care providers in a foreign country. (3) Affiliate In this subsection, the term affiliate means a business entity that has a relationship with a second business entity if, directly or indirectly\u2014 (A) one business entity controls, or has the power to control, the other business entity; or (B) a third party controls, or has the power to control, both of the business entities. .\n#### 4. Rapid assessment tests intended to ensure proper reprocessing\n##### (a) Inclusion in device definition\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended\u2014\n**(1)**\nin paragraph (h)(1)\u2014\n**(A)**\nin clause (B), by striking or at the end;\n**(B)**\nin clause (C), by striking and at the end and inserting or ; and\n**(C)**\nby inserting after clause (C) the following:\n(D) a rapid assessment test intended to ensure the proper reprocessing of a reusable device (as defined in paragraph (tt)), and ; and\n**(2)**\nby adding at the end the following:\n(tt) The term reusable device means a device that\u2014 (1) is intended to be used more than one time; and (2) must be sanitized (whether through cleaning, disinfection, or sterilization) to ensure that the device is safe and effective for such intended use. .\n##### (b) Instructions for use and validation data\nSection 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ), as amended by sections 2 and 3 of this Act, is further amended by adding at the end the following:\n(t) Instructions for use and validation data (1) Initial list Not later than 1 year after the date of enactment of this subsection, the Secretary shall by regulation develop and publish a list of types of rapid assessment tests described in section 201(h)(1)(D) for which reports under subsection (k) must include\u2014 (A) instructions for use that have been validated in a manner specified by the Secretary; and (B) validation data, of the types specified by the Secretary. (2) Updates The Secretary shall by regulation periodically update the list required by paragraph (1). (3) Enforcement Beginning on the date of publication of the initial list under paragraph (1), the Secretary shall not accept any notification under subsection (k) for clearance of a type of rapid assessment test that is included on such list unless such notification includes instructions for use and validation data in accordance with paragraph (1). .",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-04-07T13:05:58Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2372ih.xml"
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
      "title": "DEVICE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEVICE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disclosure; and Encouragement of Verification, Innovation, Cleaning, and Efficiency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to enhance medical device communications and ensure device cleanliness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:48Z"
    }
  ]
}
```
