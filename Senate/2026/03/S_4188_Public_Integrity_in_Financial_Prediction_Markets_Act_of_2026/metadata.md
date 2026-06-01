# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4188
- Title: Public Integrity in Financial Prediction Markets Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4188
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-09T14:04:34Z
- Update date including text: 2026-04-23T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4188",
    "number": "4188",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Public Integrity in Financial Prediction Markets Act of 2026",
    "type": "S",
    "updateDate": "2026-04-09T14:04:34Z",
    "updateDateIncludingText": "2026-04-23T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:14:56Z",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IN"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4188is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4188\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Ms. Slotkin (for herself, Mr. Young , Mr. Schiff , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit a covered individual from engaging in covered transactions involving prediction market contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Integrity in Financial Prediction Markets Act of 2026 .\n#### 2. Prohibition on covered transactions involving prediction market contracts\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Prohibited covered transactions involving prediction market contracts 13151. Definitions In this subchapter: (1) Covered individual The term covered individual means\u2014 (A) the President; (B) the Vice President; (C) a Member of Congress; (D) a House of Representatives or Senate employee; (E) a political appointee; or (F) an employee of an Executive agency or independent regulatory agency. (2) Covered transaction The term covered transaction means the purchase, sale, or exchange of any prediction market contract. (3) Executive agency The term Executive agency has the meaning given the term in section 105 of title 5. (4) House of Representatives or Senate employee The term House of Representatives or Senate employee \u2014 (A) means an employee of the Federal Government whose pay is disbursed by the Secretary of the Senate or the Chief Administrative Officer of the House of Representatives; and (B) does not include an employee described in subparagraph (A) who is serving under a temporary or term appointment. (5) Independent regulatory agency The term independent regulatory agency has the meaning given the term in section 3502 of title 44. (6) Material nonpublic information The term material nonpublic information means information\u2014 (A) that a reasonable investor would consider important in making a decision relating to a prediction market contract; and (B) that is not publicly available. (7) Member of Congress; supervising ethics office The terms Member of Congress and supervising ethics office have the meanings given those terms in section 13101. (8) Political appointee The term political appointee has the meaning given the term in section 106(f)(5) of title 49. (9) Prediction market contract The term prediction market contract means any financial instrument, contract, or derivative\u2014 (A) listed on or offered by a platform, regardless of whether the platform is domiciled in the United States; and (B) tied to the occurrence or non-occurrence of an event, including event contracts, as described in section 5c(c)(5)(C)(i) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132(c)(5)(C)(i) ). 13152. Prohibition No covered individual may use material nonpublic information derived from the position of the covered individual as President, Vice President, a Member of Congress, a House of Representatives or Senate employee, a political appointee, or an employee of an Executive agency or independent regulatory agency or gained from the performance of the official responsibilities of the covered individual as a means for making a profit through a covered transaction. 13153. Penalties (a) In general Notwithstanding any other provision of law, including any regulation, a covered individual who violates section 13152 shall be assessed a fine not to exceed the greater of\u2014 (1) $500; or (2) an amount equal to double the profit made by the covered individual through the applicable covered transaction. (b) Deposit in Treasury The fines paid under subsection (a) shall be deposited in the miscellaneous receipts of the Treasury. 13154. Duties of supervising ethics offices Not later than 180 days after the date of enactment of the Public Integrity in Financial Prediction Markets Act of 2026 , each supervising ethics office shall\u2014 (a) impose and collect penalties in accordance with section 13153; (b) establish such procedures and standard forms as the supervising ethics office determines appropriate to implement this subchapter; (c) in consultation with the Commodity Futures Trading Commission, issue such rules and guidelines as the supervising ethics office determines appropriate for the implementation and application of this subchapter; and (d) publish on a website all procedures, forms, rules, and guidelines described in this section. 13155. Reports Not later than 30 days after receiving notification of any covered transaction the value of which is more than $250 and to which the covered individual is a party, the covered individual shall submit to the applicable supervising ethics office a report describing the covered transaction, which shall include\u2014 (1) the value of the prediction market contract, including the purchase price and number of prediction market contracts purchased; (2) the date and time of the covered transaction; (3) the name of the prediction market contract and the position taken on the prediction market contract; (4) the prediction market contract trading platform used to complete the covered transaction; and (5) the profit or loss of the covered transaction after the prediction market contract closes, or the covered individual exits the position, provided that if the prediction market contract is not closed on the date on which the report under this section is submitted, an additional report shall be submitted not later than 30 days after the date on which the prediction market contract closes or the covered individual exits the position. .\n##### (b) Clerical amendment\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Prohibited covered transactions involving prediction market contracts 13151. Definitions. 13152. Prohibition. 13153. Penalties. 13154. Duties of supervising ethics offices. 13155. Reports. .",
      "versionDate": "2026-03-25",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-09T14:04:33Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4188is.xml"
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
      "title": "Public Integrity in Financial Prediction Markets Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Integrity in Financial Prediction Markets Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit a covered individual from engaging in covered transactions involving prediction market contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:40Z"
    }
  ]
}
```
