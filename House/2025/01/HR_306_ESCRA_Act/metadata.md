# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/306
- Title: ESCRA Act
- Congress: 119
- Bill type: HR
- Bill number: 306
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-04-15T08:05:51Z
- Update date including text: 2026-04-15T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/306",
    "number": "306",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001238",
        "district": "",
        "firstName": "Sarah",
        "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
        "lastName": "McBride",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "ESCRA Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:51Z",
    "updateDateIncludingText": "2026-04-15T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:36:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "PA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr306ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 306\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. McBride (for herself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Credit Repair Organizations Act to add additional protections against harmful practices within the credit repair organization industry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ending Scam Credit Repair Act or the ESCRA Act .\n#### 2. Credit Repair Organization definition\nSection 403(3) of the Credit Repair Organizations Act ( 15 U.S.C. 1679a(3) )\u2014\n**(1)**\nin subparagraph (A), by inserting (not including anything received in return for representing a consumer in preparation for or during litigation) after consideration ; and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting an entity or individual that is, in good faith and not for the purpose of evading this title after include ;\n**(B)**\nin clause (ii), by striking or ;\n**(C)**\nin clause (iii), by striking the period and inserting ; or ; and\n**(D)**\nby adding at the end the following:\n(iv) any attorney that provides legal services rendered or to be rendered to a consumer in contemplation of or in connection with a case filed, or to be filed within 12 months, under title 11 or title 15, United States Code, by an attorney within the same law firm. .\n#### 3. Prohibited practices\n##### (a) Untrue or misleading statements\n**(1) In general**\nSection 404(a)(1) of the Credit Repair Organizations Act ( 15 U.S.C. 1679b(a)(1) ) is amended\u2014\n**(A)**\nby inserting knowingly before make any statement, or ;\n**(B)**\nin subparagraph (A), by striking or ; and\n**(C)**\nby adding at the end the following:\n(C) the Bureau of Consumer Financial Protection directly or through an online portal established to receive complaints, disputes, or reports of fraud; (D) the Federal Trade Commission directly or through an online portal established to receive complaints, disputes, or reports of fraud; or (E) any Federal, State, local, or Tribal law enforcement agency, directly or through an online portal established to receive complaints, disputes, or reports of fraud; .\n**(2) Finding**\nThe Congress finds that it is already unlawful to make materially false, fictitious, or fraudulent statements or representations to the Bureau of Consumer Financial Protection.\n##### (b) Additional prohibited practices\nSection 404 of the Credit Repair Organizations Act ( 15 U.S.C. 1679b ) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (B)(ii), by inserting or after credit; ; and\n**(B)**\nby adding at the end the following:\n(C) the Bureau of Consumer Financial Protection or the Federal Trade Commission; ;\n**(2)**\nby amending subsection (b) to read as follows:\n(b) Payment in Advance (1) In general No credit repair organization may request or receive payment of any fee or consideration from a consumer for services represented to remove derogatory or inaccurate information from, or improve, such consumer's credit history, credit record, or credit rating, or services related to such a representation, until the credit repair organization has provided such consumer with documentation in the form of a consumer report, issued not less than 6 months after such service, from a consumer reporting agency that demonstrates that such representation has been achieved. (2) Rule of construction Nothing in this subsection shall be construed to alter the permissible purposes of furnishing a consumer report described in section 604 of the Fair Credit Reporting Act. ; and\n**(3)**\nby adding at the end the following:\n(c) Jamming A credit repair organization may not submit multiple disputes described in section 611 of the Fair Credit Reporting Act of the same information unless all of the following are true: (1) The consumer reporting agency or data furnisher has had the time permitted under the Fair Credit Reporting Act to conduct a reasonable investigation on the prior dispute. (2) The consumer reporting agency or data furnisher has returned the results of its investigation to the consumer with respect to such dispute, unless there are material changes to the information submitted with the dispute. (3) The credit repair organization includes with the resubmitted dispute a specific description of what information is inaccurate. .\n#### 4. Disclosures\nSection 405 of the Credit Repair Organizations Act ( 15 U.S.C. 1679c ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking due to fraud. and inserting due to fraud. Credit repair organizations do not provide any services that you cannot do yourself for free. ;\n**(B)**\nby striking regulates and inserting and the Bureau of Consumer Financial Protection regulate ; and\n**(C)**\nby inserting The Bureau of Consumer Financial Protection 1700 G St. NW, Washington, DC, 20552 Tel: 855\u2013411\u20132372 TTY/TTD: 855\u2013729\u20132372 after 20580 ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking the period at the end and inserting and any recordings of telephone communications with the consumer. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking 2 in the heading and inserting 5 ;\n**(ii)**\nby inserting and any telephone recordings with the consumer after consumer\u2019s statement ;\n**(iii)**\nby striking 2 and inserting 5 ; and\n**(iv)**\nby striking statement is signed by the consumer and inserting statement or the telephone recordings are created .\n#### 5. Consumer contract required\n##### (a) In general\nSection 407(c) of the Credit Repair Organizations Act ( 15 U.S.C. 1679e(c) ) is amended by adding at the end the following:\n(3) copies of all communications sent on behalf of the consumer, at the time the communication is sent. .\n##### (b) Technical amendment\nSection 407(c) of the Credit Repair Organizations Act ( 15 U.S.C. 1679e(c) ) is amended\u2014\n**(1)**\nby striking at the time the contract or the other document is signed. ;\n**(2)**\nin paragraph (1), by striking ; and inserting , at the time the contract or the other document is signed; ; and\n**(3)**\nin paragraph (2), by adding at the end at the time the contract or the other document is signed; and .\n#### 6. Noncompliance\nSection 408 of the Credit Repair Organizations Act ( 15 U.S.C. 1679f ) is amended by adding at the end following:\n(d) Legal services within credit repair organizations A credit repair organization shall be subject to this title regardless of whether the organization is, or employs, an attorney who also provides legal services to a consumer, except if such attorney is an attorney described in section 403(3)(B)(iv). (e) Credit repair organizations without a State license On or after January 1, 2026, no person may act as a credit repair organization unless such person is licensed by a State. .\n#### 7. Credit repair organization communications with furnishers of information\n##### (a) In general\nThe Credit Repair Organizations Act ( 15 U.S.C. 1679 et seq. ) is amended by inserting after section 408 the following new section:\n408A. Credit repair organization communications with furnishers of information Disputes submitted to a person who furnishes information to a consumer reporting agency by or on behalf of a credit repair organization shall meet the following requirements: (1) If sent by mail, the dispute shall be transmitted by first class mail and list on the envelope the\u2014 (A) name of the credit repair organization; and (B) State license number of the credit repair organization, if applicable. (2) The dispute shall list the\u2014 (A) name of the credit repair organization; (B) State license number of the credit repair organization, if applicable; and (C) name of the consumer on whose behalf the dispute is submitted. (3) In the case of any additional communication after an initial dispute, the additional communication shall clearly and conspicuously identify any material changes to the information provided in the initial written dispute and include the information described in paragraphs (1) and (2). (4) In the case where a credit repair organization sells or otherwise provides an online or paper blank dispute form to be completed and filed by the consumer, such form must contain the\u2014 (A) name and address of such credit repair organization; and (B) State license number of such credit repair organization, if applicable. (5) In the case where the person responds to a dispute submitted by a credit repair organization seeking clarifying information, verifying if the customer has actually engaged with the credit repair organization, or denying the accuracy of the underlying claim, the credit repair organization shall respond in writing within 15 business days. (6) In the case where the credit repair organization is an attorney, the attorney shall certify that any communication is consistent with any information or documentation provided by the consumer, confirmed based upon methods or means proven to be historically reliable and accurate. (7) A credit repair organization, when sending a dispute, shall disclose the fact that it is a credit repair organization by placing the following disclosure on the dispute letter: This communication was submitted or prepared on behalf of the consumer by a credit repair organization, as defined in section 403 of the Credit Repair Organizations Act ( 15 U.S.C. 1679a ). .\n##### (b) Clerical amendment\nThe table of contents for the Credit Repair Organizations Act is amended by inserting after the item relating to section 408 the following:\n408A. Credit repair organization communications with furnishers of information. .\n#### 8. Civil liability\nSection 409(a)(1) of the Credit Repair Organizations Act ( 15 U.S.C. 1679g(a)(1) ) is amended\u2014\n**(1)**\nby striking Actual damages and inserting Damages ;\n**(2)**\nin subparagraph (A), by striking or ;\n**(3)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(4)**\nby adding at the end the following:\n(C) the amount of $500 in damages for each violation of this title. .",
      "versionDate": "2025-01-09",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-27T22:20:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr306",
          "measure-number": "306",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr306v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ending Scam Credit Repair Act or the ESCRA Act</strong></p><p>This bill revises the Credit Repair Organizations Act and creates additional requirements for credit repair organizations (CROs).</p><p>Under current law, it is illegal for a person (including a\u00a0CRO) to make false or misleading statements regarding a consumer\u2019s creditworthiness or standing to a consumer reporting agency or to a consumer credit provider. The bill additionally prohibits making such statements to the Consumer Financial Protection Bureau, the Federal Trade Commission, or law enforcement. To be subject to this prohibition, the bill also requires such statements to be made knowingly.</p><p>The bill also revises CRO obligations to consumers. A CRO is prohibited from charging a consumer for a service (e.g., getting inaccurate information removed from a credit report) until the CRO provides proof of success not less than six months after providing the service. The bill also requires\u00a0additional disclosures to consumers, requires the retention of any recorded telephone calls, and increases the time records must be retained from two to five years. In addition, consumers must be given copies of all communications sent on their behalf.</p><p>Under the bill, all persons must be licensed by a state to act as a\u00a0CRO. The bill also restricts a CRO\u2019s ability to submit multiple credit disputes regarding the same information.</p><p>The bill also sets a minimum liability amount for damages of $500 for each violation of the Credit Repair Organizations Act.</p>"
        },
        "title": "ESCRA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr306.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Scam Credit Repair Act or the ESCRA Act</strong></p><p>This bill revises the Credit Repair Organizations Act and creates additional requirements for credit repair organizations (CROs).</p><p>Under current law, it is illegal for a person (including a\u00a0CRO) to make false or misleading statements regarding a consumer\u2019s creditworthiness or standing to a consumer reporting agency or to a consumer credit provider. The bill additionally prohibits making such statements to the Consumer Financial Protection Bureau, the Federal Trade Commission, or law enforcement. To be subject to this prohibition, the bill also requires such statements to be made knowingly.</p><p>The bill also revises CRO obligations to consumers. A CRO is prohibited from charging a consumer for a service (e.g., getting inaccurate information removed from a credit report) until the CRO provides proof of success not less than six months after providing the service. The bill also requires\u00a0additional disclosures to consumers, requires the retention of any recorded telephone calls, and increases the time records must be retained from two to five years. In addition, consumers must be given copies of all communications sent on their behalf.</p><p>Under the bill, all persons must be licensed by a state to act as a\u00a0CRO. The bill also restricts a CRO\u2019s ability to submit multiple credit disputes regarding the same information.</p><p>The bill also sets a minimum liability amount for damages of $500 for each violation of the Credit Repair Organizations Act.</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr306"
    },
    "title": "ESCRA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Scam Credit Repair Act or the ESCRA Act</strong></p><p>This bill revises the Credit Repair Organizations Act and creates additional requirements for credit repair organizations (CROs).</p><p>Under current law, it is illegal for a person (including a\u00a0CRO) to make false or misleading statements regarding a consumer\u2019s creditworthiness or standing to a consumer reporting agency or to a consumer credit provider. The bill additionally prohibits making such statements to the Consumer Financial Protection Bureau, the Federal Trade Commission, or law enforcement. To be subject to this prohibition, the bill also requires such statements to be made knowingly.</p><p>The bill also revises CRO obligations to consumers. A CRO is prohibited from charging a consumer for a service (e.g., getting inaccurate information removed from a credit report) until the CRO provides proof of success not less than six months after providing the service. The bill also requires\u00a0additional disclosures to consumers, requires the retention of any recorded telephone calls, and increases the time records must be retained from two to five years. In addition, consumers must be given copies of all communications sent on their behalf.</p><p>Under the bill, all persons must be licensed by a state to act as a\u00a0CRO. The bill also restricts a CRO\u2019s ability to submit multiple credit disputes regarding the same information.</p><p>The bill also sets a minimum liability amount for damages of $500 for each violation of the Credit Repair Organizations Act.</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr306"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr306ih.xml"
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
      "title": "ESCRA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ESCRA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ending Scam Credit Repair Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Credit Repair Organizations Act to add additional protections against harmful practices within the credit repair organization industry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:26Z"
    }
  ]
}
```
