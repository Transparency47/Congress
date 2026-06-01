# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2956?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2956
- Title: Used Car Safety Recall Repair Act
- Congress: 119
- Bill type: S
- Bill number: 2956
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2025-12-10T19:04:00Z
- Update date including text: 2025-12-10T19:04:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2956",
    "number": "2956",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Used Car Safety Recall Repair Act",
    "type": "S",
    "updateDate": "2025-12-10T19:04:00Z",
    "updateDateIncludingText": "2025-12-10T19:04:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T22:55:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2956is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2956\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the sale, lease, or loan of used motor vehicles with open recalls to consumers by auto dealers.\n#### 1. Short title\nThis Act may be cited as the Used Car Safety Recall Repair Act .\n#### 2. Used motor vehicle consumer protection\n##### (a) Definitions\nSection 30102(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking chapter\u2014 and inserting chapter: ;\n**(2)**\nin each of paragraphs (1) through (13)\u2014\n**(A)**\nby inserting The term after the paragraph designation; and\n**(B)**\nby inserting a paragraph heading, the text of which is comprised of the term defined in the paragraph; and\n**(3)**\nby adding at the end the following:\n(14) Used motor vehicle The term used motor vehicle means a motor vehicle that has previously been purchased other than for resale. .\n##### (b) Dealer reimbursement and limitation on the sale, lease, or loan of used motor vehicles\nSection 30120 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as paragraphs (2) and (1), respectively, and moving the paragraphs so as to appear in numerical order;\n**(B)**\nin paragraph (2) (as so redesignated), in the paragraph heading, by striking In general and inserting Reimbursement for remedy provided ; and\n**(C)**\nby adding at the end the following:\n(3) Unavailable remedy for a used motor vehicle (A) Definition of dealer In this paragraph, the term dealer has the meaning given the term in subsection (l)(1). (B) Reimbursement (i) In general If a dealer is in possession of a used motor vehicle and the manufacturer of that used motor vehicle has failed to make a remedy available by the date described in clause (ii), the manufacturer shall reimburse the dealer at the rate described in clause (iii) until the earlier of\u2014 (I) the date on which a remedy is made available by the manufacturer; and (II) the date on which the total amount of payments to a dealer under this paragraph equals the fair market value of the used motor vehicle. (ii) Date described The date referred to in clause (i) is the date that is 60 days after the date described in section 30119(b) and specified by the manufacturer\u2014 (I) in a notification under section 30119(a)(5); or (II) under section 30121(c)(2). (iii) Rate described The rate referred to in clause (i) is a rate determined by the Secretary that is not less than 1 percent of the fair market value of the used motor vehicle per month, which shall be prorated on a daily basis for each day that the used motor vehicle is in the possession of the dealer\u2014 (I) after the date described in clause (ii); and (II) before the date on which a remedy is made available by the manufacturer. (iv) Limitation The total amount of payments to a dealer under this paragraph with respect to a used motor vehicle shall not exceed the fair market value of that used motor vehicle. ; and\n**(2)**\nby adding at the end the following:\n(l) Limitation on the sale, lease, or loan of used motor vehicles (1) Definition of dealer In this subsection, the term dealer means a person that, during the 1-year period ending on the date of the sale, lease, or loan of a used motor vehicle, has sold at least 5 motor vehicles to buyers that in good faith purchased the vehicles other than for resale. (2) Limitation Except as provided under paragraph (3), a dealer shall not sell, lease, or loan a used motor vehicle until after any defect or noncompliance for which notification is required under subsection (b)(2)(A) or (c) of section 30118 with respect to the vehicle has been remedied. (3) Exception Paragraph (2) shall not apply if\u2014 (A) the recall information regarding the used motor vehicle\u2014 (i) was not available at the time of sale, lease, or loan using the means established by the Secretary under section 31301 of the Moving Ahead for Progress in the 21st Century Act ( 49 U.S.C. 30166 note; Public Law 112\u2013141 ); and (ii) was not available on the website of the manufacturer; (B) notification of the defect or noncompliance is required by an order issued by the Secretary under section 30118(b)(2), but enforcement of the order is set aside in a civil action to which section 30121(d) applies; (C) the used motor vehicle is sold at wholesale; or (D) (i) the used motor vehicle is a junk automobile (as defined in section 30501); and (ii) all required information with respect to the used motor vehicle has been reported to the National Motor Vehicle Title Information System under section 30504. .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in Senate"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-10T19:04:00Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2956is.xml"
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
      "title": "Used Car Safety Recall Repair Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Used Car Safety Recall Repair Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the sale, lease, or loan of used motor vehicles with open recalls to consumers by auto dealers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:17Z"
    }
  ]
}
```
