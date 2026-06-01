# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7015?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7015
- Title: Protecting TPLF From Abuse Act
- Congress: 119
- Bill type: HR
- Bill number: 7015
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-01-14T16:07:56Z
- Update date including text: 2026-01-14T16:07:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7015",
    "number": "7015",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Protecting TPLF From Abuse Act",
    "type": "HR",
    "updateDate": "2026-01-14T16:07:56Z",
    "updateDateIncludingText": "2026-01-14T16:07:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:02:30Z",
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
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7015ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7015\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Issa (for himself, Mr. Fitzgerald , and Mr. Baumgartner ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to protect legal proceedings from manipulation and provide for transparency and oversight of third-party beneficiaries in civil actions.\n#### 1. Short title\nThis Act may be cited as the Protecting Third Party Litigation Funding From Abuse Act or the Protecting TPLF From Abuse Act .\n#### 2. Transparency and oversight of third-party beneficiaries in civil cases\n##### (a) In general\nChapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Initial disclosures regarding third-party beneficiaries (a) In general Except as provided in subsection (b), in any civil action, a party or any counsel of record for a party shall\u2014 (1) disclose in writing to the court and all other named parties to the civil action the identity of any person (other than counsel of record) that has a legal right to receive any payment or thing of value that is contingent in any respect on the outcome or proceeds of the civil action or a group of civil actions of which the civil action is a part, including\u2014 (A) any portion of a settlement, a judgment, or an award of attorney\u2019s fees from the civil action or group of civil actions; or (B) any other proceeds from the civil action or group of civil actions; (2) produce to the court, for in camera review, any agreement creating a legal right described in paragraph (1), including any ancillary agreement or document; and (3) after the review conducted under paragraph (2), produce to each other named party to the civil action, for inspection and copying, each document produced under paragraph (2), subject to any protective order, use limitation, or any other limitation or exclusion ordered by the court, including\u2014 (A) any limitation or exclusion relating to attorney-client privilege, the attorney work product doctrine, or any other applicable privilege; or (B) any limitation or exclusion to protect from disclosure to any party or non-party the identity of any member, donor, or associate of the person that has a legal right described in paragraph (1), except to the extent that the member, donor, or associate also has a legal right to receive any payment or thing of value described in subsection (a)(1) and is not excepted from disclosure under subsection (b)(1). (b) Exceptions and limitations (1) In general The requirements under subsection (a) shall not apply with respect to a person that has a legal right to receive any payment or thing of value described in subsection (a)(1) if the legal right is solely regarding\u2014 (A) the repayment of the principal of a loan; (B) the repayment of the principal of a loan plus interest that does not exceed the higher of 10 percent or a rate three times the annual average 30-year constant maturity Treasury yield, as published by the Board of Governors of the Federal Reserve System, for the year preceding the date on which the relevant agreement was executed; (C) the reimbursement of attorney\u2019s fees paid to counsel of record for services provided in the civil action; or (D) the reimbursement of a grant. (2) Donor, member, and associate identity The requirements under subsection (a)(1) shall not apply with respect to any donor, member, or associate of the person that has a legal right described in subsection (a)(1) unless the donor, member, or associate also has a legal right to receive any payment or thing of value described in subsection (a)(1) and is not excepted from disclosure under subsection (b)(1). (3) Donor and member list The requirements under subsections (a)(2) and (a)(3) shall not require the production of lists of members, donors, or associates, and the court shall permit redactions of the identity of any member, donor, or associate from materials disclosed pursuant to subsection (a)(3), unless that member, donor, or associate also has a legal right to receive any payment or thing of value described in subsection (a)(1) and is not excepted from disclosure under subsection (b)(1). (4) Admissibility and discovery Nothing in this Section may be construed to render admissible any disclosure, document, or thing provided under this Section, or any information therein, or to affect whether any disclosure, document, or thing is discoverable except as expressly provided in this section. (c) Timing The disclosures required by subsection (a) shall be made not later than the later of\u2014 (1) 10 days after the execution of any agreement described in subsection (a)(2); (2) the time of initial disclosures made pursuant to Federal Rule of Civil Procedure 26(a)(1); or (3) the time set by the court for such disclosures. (d) Duty to correct A party or counsel of record that made a disclosure required by this section shall supplement or correct each such disclosure in a timely manner\u2014 (1) if such party or counsel of record learns that the disclosure is or has become incomplete or incorrect in some material respect, if the additional or corrective information has not otherwise been made known to the other parties during the discovery process or in writing; or (2) as ordered by the court. .\n##### (b) Clerical amendment\nThe table of sections for chapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Third-party beneficiary disclosure. .\n#### 3. Applicability\nThe amendments made by this Act shall apply to any civil action pending on or commenced after the date of enactment of this Act.",
      "versionDate": "2026-01-12",
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
        "updateDate": "2026-01-14T16:07:56Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7015ih.xml"
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
      "title": "Protecting TPLF From Abuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T09:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting TPLF From Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Third Party Litigation Funding From Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to protect legal proceedings from manipulation and provide for transparency and oversight of third-party beneficiaries in civil actions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T09:18:31Z"
    }
  ]
}
```
