# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8309?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8309
- Title: To amend title 28, United States Code, to prohibit Presidents and Vice Presidents from receiving damages payments from the United States, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8309
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-29T08:07:27Z
- Update date including text: 2026-04-29T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8309",
    "number": "8309",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "To amend title 28, United States Code, to prohibit Presidents and Vice Presidents from receiving damages payments from the United States, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:27Z",
    "updateDateIncludingText": "2026-04-29T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:02:10Z",
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
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8309ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8309\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Raskin (for himself and Mr. Min ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to prohibit Presidents and Vice Presidents from receiving damages payments from the United States, and for other purposes.\n#### 1. Settlement payments\n##### (a) In general\nChapter 161 of title 28, United States Code, is amended by adding at the end the following:\n2417. Rules for payments to current and former Presidents and Vice Presidents (a) Definitions In this section, the term covered individual means\u2014 (1) the President; (2) the Vice President; (3) a former President if the former Vice President of the former President is President; (4) the spouse or dependent child of an individual described in paragraphs (1) through (3); and (5) a trust (or a trustee acting on behalf of a trust) or any other legal vehicle or entity established, or serving, for the benefit of, or owned or controlled by, an individual described in paragraphs (1) through (4). (b) Ban on covered individuals obtaining settlement payments from the United States Notwithstanding any other provision of law, no covered individual may\u2014 (1) recover or agree to recover damages, reimbursement, payment of attorney\u2019s fees, or any other payment, whether monetary or in kind, from the United States related to any administrative claim, civil action, or other claim against the United States through a settlement agreement, consent decree, administrative resolution of the claim, or similar arrangement; or (2) direct any payment described in paragraph (1) to be made to a third party. (c) Ban on filing administrative claims seeking damages No covered individual may file an administrative claim against the United States seeking to recover damages, reimbursement, payment of attorney\u2019s fees, or any other payment, whether monetary or in kind, from the United States. (d) Administrative processing and making of payments No department or agency of the United States may administratively process or fulfill a claim for damages, reimbursement, payment of attorney\u2019s fees, or any other payment, whether monetary or in kind, filed by or on behalf of a covered individual, through a settlement agreement, consent decree, administrative resolution of the claim, or similar arrangement. (e) Guardrails for lawsuits seeking damages Notwithstanding any other provision of law, a court\u2014 (1) may not award any damages other than actual or compensatory damages to a covered individual in a civil action against the United States under any other provision of law; and (2) may award actual or compensatory damages to a covered individual in a civil action against the United States under any other provision of law only if\u2014 (A) the covered individual agrees to the court appointment of an independent counsel, removable only by the court for cause, to represent the agency defending against the claim of the covered individual; (B) the court appoints an independent counsel under subparagraph (A); and (C) subject to the continued supervision of the court, any agency involved in the litigation cooperates with the independent counsel appointed under subparagraph (A), including by facilitating access to documents and employees necessary to complete the work of the independent counsel. (f) Transparency requirement In any action brought under subsection (e), the court shall make public and free of charge, via an online, publicly accessible, and user-friendly method all filings and proceedings in an action described in subsection (e), including through making the audio of each session conducted by the court during the proceedings available online contemporaneously with the session. (g) Guardrails for former covered individuals After a President or Vice President leaves office, that former President or Vice President or other former covered individual described in paragraphs (3) through (5) of subsection (a) may file an administrative claim or suit against the United States and the United States may adjudicate or settle such claim or suit, if\u2014 (1) the agency or department against which the claim or suit is filed appoints an expert, career employee who can only be removed for good cause to lead any review and adjudication of the claim during any administrative or settlement process; (2) no executive branch employee or official appointed by a covered individual participates in any capacity in reviewing, litigating against, or adjudicating the claim or settlement; (3) for any agreement to make a payment from the United States to a former covered individual, the terms of the agreement are published in the Federal Register not later than 7 days after the date on which the agreement is entered; (4) for any payment from the United States to a former covered individual, the amount, date, and form of payment is published in the Federal Register not later than 7 days after the date on which the payment is made; and (5) the agency or department against which the claim or suit is filed submits to the appropriate congressional committees of the Senate and the House of Representatives a copy of\u2014 (A) the claim or suit prior to assessing the claim or suit; and (B) any resulting approval or denial of the claim or settlement concurrently with notification to the claimant. (h) Penalties (1) In general A covered individual who willfully violates subsection (b) or knowingly violates subsection (c) shall be subject to disgorgement of the payment, civil penalties of not more than the greater of $1,000,000 or an amount that is equal to the aggregate amount of any payment or payments, imprisonment for not more than 5 years, or any combination thereof. (2) Officers and employees Any individual who willfully causes a department of agency to violate subsection (d) shall be subject to civil penalties of not more than $50,000, imprisonment for not more than 6 months, or both. (i) Limitations (1) Statute of limitations for enforcement of this act No person shall be prosecuted, tried, or punished, or made subject to civil monetary penalties, for a violation of this section, unless the indictment is found or the information is instituted within 10 years after such offense shall have been committed. (2) Tolling of statute of limitations for underlying claims The limitations period for any claim a covered individual seeks to bring against the United States shall be tolled during the period beginning on the date on which the individual becomes a covered individual and ending on the day after the date on which the term in office of the covered individual expires. (j) Applicability This section shall apply to any request for, processing of a request for, or recovery of damages, reimbursement, payment of attorney\u2019s fees, or other payment, whether monetary or in kind, occurring after the date of enactment of this section, regardless of when the related claim or cause of action arose. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 161 of title 28, United States Code, is amended by adding at the end the following:\n2417. Rules for payments to current and former Presidents and Vice Presidents. .",
      "versionDate": "2026-04-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-15",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "4299",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ban Presidential Plunder of Taxpayer Funds Act",
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
        "name": "Law",
        "updateDate": "2026-04-22T18:42:16Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8309ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to prohibit Presidents and Vice Presidents from receiving damages payments from the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:32Z"
    },
    {
      "title": "To amend title 28, United States Code, to prohibit Presidents and Vice Presidents from receiving damages payments from the United States, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T08:06:43Z"
    }
  ]
}
```
