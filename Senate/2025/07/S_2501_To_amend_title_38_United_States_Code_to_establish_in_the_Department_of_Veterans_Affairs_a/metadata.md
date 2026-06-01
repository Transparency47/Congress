# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2501
- Title: VSAFE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2501
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-12-05T21:30:52Z
- Update date including text: 2025-12-05T21:30:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2501",
    "number": "2501",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "VSAFE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:30:52Z",
    "updateDateIncludingText": "2025-12-05T21:30:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T16:32:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NH"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AR"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2501is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2501\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Cornyn (for himself, Ms. Hassan , Mr. Boozman , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish in the Department of Veterans Affairs a Veterans Scam and Fraud Evasion Officer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Scam And Fraud Evasion Act of 2025 or the VSAFE Act of 2025 .\n#### 2. Veterans Scam and Fraud Evasion Officer\n##### (a) In general\nChapter 3 of title 38, United States Code, is amended by adding at the end the following new section:\n325. Veterans Scam and Fraud Evasion Officer (a) Establishment There is in the Department a Veterans Scam and Fraud Evasion Officer, who shall\u2014 (1) be responsible for fraud and scam prevention, reporting, and incident response plans at the Department; and (2) serve as a central point of contact to direct veterans to resources to prevent and mitigate fraud and scams. (b) Responsibilities The Veterans Scam and Fraud Evasion Officer shall carry out the following responsibilities: (1) Providing comprehensive communication from the Secretary to employees of the Department and veterans, their families, caregivers, and survivors during strategic and time-sensitive fraud and scam incidents. (2) Establishing consistent guidance across the enterprise for employees as well as veterans, their families, caregivers, and survivors on how to identify, report, and avoid fraud and scam attempts. (3) Promoting the VSAFE Fraud Hotline and VSAFE.gov website of the Department (and any successor resources) and identifying other identity theft resources available to veterans, their families, caregivers, and survivors, including with respect to actions made by the Secretary to protect the identities of veterans and their beneficiaries. (4) Developing methods to monitor fraud and scam metrics within the Department\u2014 (A) to provide internal and external reporting; (B) to enable advanced data analytics; and (C) to facilitate proactive and robust fraud and scam trend identification. (5) Developing comprehensive training plans for Department employees fielding fraud and scam inquiries and reports. (6) Coordinating with the Inspector General of the Department and other Federal departments and agencies, including the Executive Office of the President, the Office of Management and Budget, the Internal Revenue Service, the Department of Justice, the Department of State, the Consumer Financial Protection Bureau, the Department of Defense, the Department of Education, the Social Security Administration, and other relevant agencies\u2014 (A) to develop a whole-of-government view within the Department to improve fraud prevention efforts within the Department; (B) to identify the proper avenues for veterans to report fraud attempts and receive assistance; and (C) to identify opportunities for coordination with such departments and agencies. (7) Consulting with veterans service organizations and State, local, and tribal governments, as necessary, to improve understanding of potential fraud and scam risks to veterans. (c) Full-Time employees Nothing in this section shall be construed to authorize an increase in the number of full-time employees otherwise authorized for the Department. (d) Rule of construction Nothing in this section shall be construed to limit the authority of the Office of Inspector General of the Department as otherwise provided in this title or in chapter 4 of title 5 (commonly referred to as the Inspector General Act of 1978). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new item:\n325. Veterans Scam and Fraud Evasion Officer. .\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting January 30, 2032 .",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-09-02",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "2683",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "VSAFE Act of 2025",
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
        "updateDate": "2025-09-05T17:12:23Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2501is.xml"
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
      "title": "VSAFE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VSAFE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Scam And Fraud Evasion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish in the Department of Veterans Affairs a Veterans Scam and Fraud Evasion Officer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:44Z"
    }
  ]
}
```
