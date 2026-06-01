# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4036?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4036
- Title: No Shorting America Act
- Congress: 119
- Bill type: HR
- Bill number: 4036
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-22T12:22:51Z
- Update date including text: 2025-07-22T12:22:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4036",
    "number": "4036",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "No Shorting America Act",
    "type": "HR",
    "updateDate": "2025-07-22T12:22:51Z",
    "updateDateIncludingText": "2025-07-22T12:22:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4036ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4036\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Kean (for himself and Ms. Craig ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend title 5, United States Code, to prohibit the short sale of certain financial investments by Members of Congress and their spouses and dependents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Shorting America Act .\n#### 2. Prohibition of congressional short selling of financial investments\nChapter 131 of title 5, United States Code, is amended by adding at the end the following (and by conforming the table of contents for such chapter accordingly):\nIV Prohibition on Congressional Short Selling 13151. Definitions In this subchapter: (1) Covered financial instrument The term covered financial instrument means\u2014 (A) any investment in\u2014 (i) a security (as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (ii) a security future (as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); or (iii) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (B) any economic interest comparable to an interest described in subclause (I) that is acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means. (2) Covered individual The term covered individual means any of the following: (A) A Member of Congress. (B) The spouse of a Member of Congress. (C) The dependent of a Member of Congress. (3) Dependent The term dependent has the meaning given that term in section 13101. (4) Member of Congress The term Member of Congress has the meaning given that term in section 13101. (5) Short sale The term short sale has the meaning given that term in section 242.200 of title 17, Code of Federal Regulations (or any successor regulation). (6) Supervising ethics office The term supervising ethics office has the meaning given that term in section 13101. 13152. Limitation on short sale (a) In general No covered individual may engage in a short sale of any covered financial instrument issued by any business entity that is listed on a national stock exchange. (b) Income tax A loss from a short sale involving a covered financial instrument that is conducted in violation of this section may not be deducted from the amount of income tax owed by the covered individual. (c) Proof of compliance (1) Submission A Member of Congress shall submit to the supervising ethics office a pledge of compliance with the requirements of this subchapter, and shall produce, upon request of the supervising ethics office, material or information determined by the supervising ethics committee to be necessary to indicate compliance with the provisions of this subchapter. (2) Certificate The supervising ethics office shall provide each Member of Congress in compliance with the provisions of this chapter with a certificate of compliance. (3) Publication The supervising ethics office shall make available, on a publicly accessible website, all certificates issued under this subsection. 13153. Enforcement (a) Referral The supervising ethics office shall refer to the Attorney General the name of any covered individual who such office has reasonable cause to believe has willfully failed to comply with the requirements of section 13152. (b) Penalty (1) In general The Attorney General may bring a civil action in any appropriate United States district court against any covered individual who knowingly and willfully fails to comply with section 13152. The court in which such action is brought may assess against such individual a civil penalty in any amount, not to exceed $50,000. (2) Limitation A covered individual may not pay any penalty resulting from a civil action under paragraph (1) using\u2014 (A) funds from a Members\u2019 Representational Allowance or Senators\u2019 Official Personnel and Office Expense Account (as the case may be); or (B) funds of any political committee under the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ). .",
      "versionDate": "2025-06-17",
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
        "name": "Congress",
        "updateDate": "2025-07-22T12:22:51Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4036ih.xml"
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
      "title": "No Shorting America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Shorting America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to prohibit the short sale of certain financial investments by Members of Congress and their spouses and dependents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:20Z"
    }
  ]
}
```
