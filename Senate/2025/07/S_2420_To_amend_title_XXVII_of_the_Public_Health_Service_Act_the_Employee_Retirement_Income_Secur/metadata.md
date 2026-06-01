# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2420
- Title: No Surprises Act Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 2420
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:48:36Z
- Update date including text: 2025-12-05T22:48:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2420",
    "number": "2420",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "No Surprises Act Enforcement Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:36Z",
    "updateDateIncludingText": "2025-12-05T22:48:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T21:03:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2420is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2420\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Marshall (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title XXVII of the Public Health Service Act, the Employee Retirement Income Security Act of 1974, and the Internal Revenue Code of 1986 to increase penalties for group health plans, health insurance issuers, and nonparticipating providers or facilities for practices that violate balance billing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Surprises Act Enforcement Act .\n#### 2. Increasing penalties for group health plans and health insurance issuers for practices that violate balance billing requirements\n##### (a) PHSA\nSection 2723(b)(2)(C) of the Public Health Service Act ( 42 U.S.C. 300gg\u201322(b)(2)(C) ) is amended\u2014\n**(1)**\nin clause (i), by inserting (or, in the case of such a failure with respect to a provision specified in clause (iv), $10,000 per violation) after $100 ; and\n**(2)**\nby adding at the end the following new clause:\n(iv) Provisions specified For purposes of clause (i), the provisions specified in this clause are the following: (I) Subparagraphs (A) and (B) of section 2799A\u20131(a)(1). (II) Clauses (i), (ii), (iii), and (v) of section 2799A\u20131(a)(1)(C). (III) Subparagraphs (A), (B), and (E) of section 2799A\u20131(b)(1). (IV) Paragraphs (1) and (2) of section 2799A\u20132(a). .\n##### (b) ERISA\nSection 502 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1131 ) is amended\u2014\n**(1)**\nin subsection (a)(6), by striking or (9) and inserting (9), or (12) ;\n**(2)**\nin subsection (b)(3)\u2014\n**(A)**\nby inserting , (c)(12), after subsections (c)(9) ; and\n**(B)**\nby inserting or (c)(12) after under subsection (c)(9) ; and\n**(3)**\nin subsection (c), by adding at the end the following new paragraph:\n(12) The Secretary may assess a civil penalty against any group health plan or health insurance issuer offering group health insurance coverage of not more than $10,000 per violation for each individual with respect to which such plan or coverage fails to comply with one of the following provisions: (A) Subparagraphs (A) and (B) of section 716(a)(1). (B) Clauses (i), (ii), (iii), and (v) of section 716(a)(1)(C). (C) Subparagraphs (A), (B), and (E) of section 716(b)(1). (D) Paragraphs (1) and (2) of section 717(a). .\n##### (c) IRC\nSection 4980D(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1), by inserting (or, in the case of such a failure with respect to a provision specified in paragraph (4), $10,000) after $100 ; and\n**(2)**\nby adding at the end the following new paragraph:\n(4) Provisions specified For purposes of paragraph (1), the provisions specified in this paragraph are the following: (A) Subparagraphs (A) and (B) of section 9816(a)(1). (B) Clauses (i), (ii), (iii), and (v) of section 9816(a)(1)(C). (C) Subparagraphs (A), (B), and (E) of section 9816(b)(1). (D) Paragraphs (1) and (2) of section 9817(a). .\n#### 3. Additional penalties for late payment or non-payment after IDR entity payment determination\n##### (a) PHSA\n**(1) Emergency and nonemergency services**\nSection 2799A\u20131(c)(6) of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111(c)(6) ) is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan or coverage the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan or coverage, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or coverage or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan or coverage, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or coverage or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan or coverage (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(1)(C)(iv)(I) or (b)(1)(C), as applicable; and (II) the out-of-network rate (as defined in subsection (a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n**(2) Air ambulance services**\nSection 2799A\u20132(b)(6) of the Public Health Service Act ( 42 U.S.C. 300gg\u2013112(b)(6) ) is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan or coverage the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan or coverage, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or coverage or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan or coverage, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or coverage or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan or coverage (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(3)(A); and (II) the out-of-network rate (as defined in section 2799\u20131(a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n##### (b) ERISA\n**(1) Emergency and nonemergency services**\nSection 716(c)(6) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185e(c)(6) ) is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan or coverage the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan or coverage, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or coverage or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan or coverage, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or coverage or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan or coverage (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(1)(C)(iv)(I) or (b)(1)(C), as applicable; and (II) the out-of-network rate (as defined in subsection (a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n**(2) Air ambulance services**\nSection 717(b)(6) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185f(b)(6) ) is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan or coverage the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan or coverage, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or coverage or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan or coverage, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or coverage or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan or coverage (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(3)(A); and (II) the out-of-network rate (as defined in section 716(a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n##### (c) IRC\n**(1) Emergency and nonemergency services**\nSection 9816(c)(6) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(1)(C)(iv)(I) or (b)(1)(C), as applicable; and (II) the out-of-network rate (as defined in subsection (a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n**(2) Air ambulance services**\nSection 9817(b)(6) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin the paragraph heading, by inserting ; penalty for late payment or non-payment after payment ;\n**(B)**\nby striking The total plan and inserting the following:\n(A) Timing of payment The total plan ;\n**(C)**\nin subparagraph (A), as so inserted, by adding at the end the following new sentence: In the case such determination is an amount less than the sum of the initial payment for such item or service and any cost sharing required to be paid by the individual receiving such item or service, the nonparticipating provider or facility furnishing such item or service shall pay to such plan the difference between such determination and such sum not later than 30 days after the date on which such determination is made. ; and\n**(D)**\nby adding at the end the following new subparagraphs:\n(B) Notification In the case of a plan, or a nonparticipating provider or facility, required to make a payment pursuant to a determination described in subparagraph (A), such plan or nonparticipating provider or facility shall submit to the Secretary a notification of such payment as of the date such payment is made in a manner specified by the Secretary. (C) Penalty for late payment or non-payment (i) In general In the case of a plan, or a nonparticipating provider or facility, that has not made the required payment described in subparagraph (A) with respect to an item or service in the time period described in such subparagraph, in addition to making such payment, such plan or nonparticipating provider or facility shall also pay to the nonparticipating provider or facility or plan (as applicable) an amount that is three times the difference between\u2014 (I) the initial payment (or, in the case of a notice of denial of payment, $0) described in subsection (a)(3)(A); and (II) the out-of-network rate (as defined in section 9816(a)(3)(K)) for such item or service (less any cost sharing required to be paid by the individual receiving such item or service). (ii) Interest A late payment penalty under clause (i) shall also be subject to interest in a manner specified by the Secretary. .\n#### 4. Transparency reporting requirements\n##### (a) PHSA\nSection 2799A\u20131(a)(2)(A)(iii) of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111(a)(2)(A)(iii) ) is amended to read as follows:\n(iii) Reporting (I) Initial reporting Beginning for 2022 and ending on December 31 of the calendar year in which the No Surprises Act Enforcement Act is enacted, the Secretary shall annually submit to Congress a report on the number of plans and issuers with respect to which audits were conducted during such year pursuant to this subparagraph. (II) Subsequent reporting (aa) In general With respect to the first calendar year following the date of the enactment of the No Surprises Act Enforcement Act , not later than February 1 of such year, and every 6 months thereafter, the Secretary, in coordination with the Secretary of Labor and the Secretary of the Treasury, shall submit to the Committee on Ways and Means, the Committee on Energy and Commerce, and the Committee on Education and the Workforce of the House of Representatives, and the Committee on Finance and the Committee on Health, Education, Labor and Pensions of the Senate, a report on any audits conducted pursuant to this subparagraph during the applicable reporting period, and any enforcement actions taken during such period in accordance with the provisions of this part, including\u2014 (AA) the total number of audits conducted under this subparagraph; (BB) the number of audits conducted pursuant to clause (ii)(I); (CC) the number of complaints submitted by providers and by participants, beneficiaries, and enrollees with respect to a violation of this part; (DD) any enforcement actions taken as a result of a complaint submitted by a provider or by a participant, a beneficiary, or an enrollee, with respect to the provisions of this part; (EE) the total number of, and the aggregate dollar amount of, any civil monetary penalties issued in accordance with this part; (FF) a summary of any non-monetary corrective action taken against a group health plan or health insurance issuer offering group or individual health insurance coverage for a violation of this part; and (GG) a description of the 3 most commonly reported violations of this part. (bb) Applicable reporting period For purposes of this subclause, the term applicable reporting period means the 6 month period prior to each report submitted under item (aa). .\n##### (b) IRC\nSection 9816(a)(2)(A)(iii) of the Internal Revenue Code of 1986 is amended to read as follows:\n(iii) Reporting (I) Initial reporting Beginning for 2022 and ending on December 31 of the calendar year in which the No Surprises Act Enforcement Act is enacted, the Secretary shall annually submit to Congress a report on the number of plans with respect to which audits were conducted during such year pursuant to this subparagraph. (II) Subsequent reporting (aa) In general With respect to the first calendar year following the date of the enactment of the No Surprises Act Enforcement Act , not later than February 1 of such year, and every 6 months thereafter, the Secretary, in coordination with the Secretary of Labor and the Secretary of Health and Human Services, shall submit to the Committee on Ways and Means, the Committee on Energy and Commerce, and the Committee on Education and Workforce of the House of Representatives, and the Committee on Finance and the Committee on Health, Education, Labor and Pensions of the Senate, a report on audits performed pursuant to this subparagraph during the applicable reporting period, and any enforcement actions taken during such period in accordance with the provisions of an applicable section, including\u2014 (AA) the total number of audits conducted under this subparagraph; (BB) the number of audits conducted pursuant to clause (ii)(I); (CC) the number of complaints submitted by providers and by participants and beneficiaries with respect to a violation of an applicable section; (DD) any enforcement actions taken pursuant to a violation of an applicable section; (EE) the total number of, and the aggregate dollar amount of, any civil monetary penalties issued in accordance with an applicable section; (FF) a summary of any non-monetary corrective action taken against a group health plan for a violation of an applicable section; and (GG) a description of the 3 most commonly reported violations of an applicable section. (bb) Definitions In this subclause: (AA) Applicable reporting period The term applicable reporting period means the 6 month period prior to each report submitted under item (aa). (BB) Applicable section The term applicable section means this section and each of sections 9817 through 9825. .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4710",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Surprises Act Enforcement Act",
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
        "name": "Health",
        "updateDate": "2025-09-12T15:21:11Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2420is.xml"
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
      "title": "No Surprises Act Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Surprises Act Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XXVII of the Public Health Service Act, the Employee Retirement Income Security Act of 1974, and the Internal Revenue Code of 1986 to increase penalties for group health plans, health insurance issuers, and nonparticipating providers or facilities for practices that violate balance billing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:23Z"
    }
  ]
}
```
