# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1138?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1138
- Title: Payment Choice Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1138
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-05-12T08:05:58Z
- Update date including text: 2026-05-12T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1138",
    "number": "1138",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000612",
        "district": "6",
        "firstName": "John",
        "fullName": "Rep. Rose, John W. [R-TN-6]",
        "lastName": "Rose",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Payment Choice Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:58Z",
    "updateDateIncludingText": "2026-05-12T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:03:50Z",
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
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NJ"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "NJ"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "MD"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NJ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "LA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "IN"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NC"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "MI"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NJ"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "KY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "HI"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1138ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1138\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Rose (for himself, Mr. Norcross , Ms. Garcia of Texas , Mr. Kustoff , Mrs. Beatty , Mr. Smith of New Jersey , Mr. Ivey , Mr. Davidson , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo ensure that United States currency is treated as legal tender to be accepted as payment for purchases of goods and services at brick-and-mortar businesses throughout the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Payment Choice Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that United States currency should be treated as legal tender throughout the United States, and that every consumer should have the right to use cash as payment at retail businesses that accept in-person payments.\n#### 3. Retail businesses prohibited from refusing cash payments\n##### (a) In general\nSubchapter I of chapter 51 of title 31, United States Code, is amended by adding at the end the following:\n5104. Retail businesses prohibited from refusing cash payments (a) In general Any person engaged in the business of selling or offering goods or services at retail to the public who accepts in-person payments at a physical location (including a person accepting payments for telephone, mail, or internet-based transactions who is accepting in-person payments at a physical location)\u2014 (1) shall accept cash as a form of payment for sales made at such physical location in amounts up to and including $500 per transaction; and (2) may not charge cash-paying customers a higher price compared to the price charged to customers not paying with cash. (b) Exceptions Subsection (a) shall not apply to a person if the person\u2014 (1) is unable to accept cash because of\u2014 (A) a sale system failure that temporarily prevents processing cash payments; or (B) temporarily having insufficient cash on hand to make change; or (2) provides customers with a device that converts cash into prepaid cards on the premises if\u2014 (A) there is no fee for the use of the device; (B) the device does not require a minimum deposit of more than one dollar; (C) any funds placed onto a prepaid card using the device do not expire, except as permitted under subsection (c); (D) the device does not collect any personal identifying information from the customer; and (E) there is no fee to use the prepaid card that the device produces. (c) Inactivity With respect to a prepaid card described under paragraph (2), the person providing the card may charge an inactivity fee in association with the card if\u2014 (1) there has been no activity with respect to the card during the 12-month period ending on the date on which the inactivity fee is imposed; (2) not more than 1 inactivity fee is imposed in any 1-month period; and (3) there is clearly and conspicuously stated, on the face of the mechanism that issues the card and on the card\u2014 (A) that an inactivity fee or charge may be imposed; (B) the frequency at which such inactivity fee may be imposed; and (C) the amount of such inactivity fee. (d) Right To not accept large bills (1) In general Notwithstanding subsection (a), for the 5-year period beginning on the date of enactment of this section, this section does not require a person or entity to accept cash payments in $50 bills or any larger bill. (2) Rulemaking (A) In general The Secretary of the Treasury shall issue a rule on the date that is 5 years after the date of the enactment of this section with respect to any bill denominations a person is not required to accept. (B) Requirement When issuing a rule under subparagraph (A), the Secretary shall require persons to accept $1, $5, $10, and $20 bills. (e) Enforcement (1) Preventative relief (A) In general Whenever any person has engaged, or there are reasonable grounds to believe that any such person is about to engage, in any act or practice prohibited by this section, any customer or prospective customer of such person aggrieved by such violation or threatened violation may deliver to the person, or cause to be so delivered by certified mail, with proof of delivery, a notice describing, in reasonable detail, the conduct or events constituting the violation or threatened violation, and giving notice that, unless such conduct is corrected or cured within 45 days after the date of delivery of such notice, a civil action for preventive relief, including an application for a permanent or temporary injunction, restraining order, or other appropriate such relief, which may include a civil penalty as hereinafter provided for, may be brought against such person. (B) Response; cure If, within the 45-day period described under subparagraph (A), the person described in that subparagraph establishes to the customer or prospective customer\u2019s reasonable satisfaction, in a response provided in writing to the customer or prospective customer, that no violation occurred as alleged, or certifies that the violation alleged has been corrected or cured, and provides reasonable assurance that no such violation henceforth will be permitted to occur in the conduct of the person\u2019s business, no further proceedings under this section may be undertaken. (C) Civil action If a person described under subparagraph (A), having received a notice described in that subparagraph, fails to respond in accordance with subparagraph (B), or responds but fails to reasonably establish that the violation alleged either did not occur or has been corrected or cured, the aggrieved customer or prospective customer shall be entitled to file a civil action against the person seeking relief as provided under this subsection. In any such filing, the customer or prospective customer shall attach to the complaint in such action copies of the notice given to the person pursuant to subparagraph (A) and the response, if any, received from such person. (2) Damages and civil penalties Any person who violates this section shall\u2014 (A) be liable for actual damages, together with, if actual damages are less than $250, liquidated damages of $250; and (B) a civil penalty of not more than $500 for a first offense and not more than $1,500 for a second or subsequent offense. (3) Jurisdiction An action under this subsection may be brought in any United States district court, or in any other court of competent jurisdiction. (4) Intervention of Attorney General Upon timely application, a court may, in its discretion, permit the Attorney General to intervene in a civil action brought under this subsection, if the Attorney General certifies that the action is of general public importance. (5) Authority to appoint court-paid attorney Upon application by an individual and in such circumstances as the court may determine just, the court may appoint an attorney for such individual and may authorize the commencement of a civil action under this subsection without the payment of fees, costs, or security. (6) Attorney\u2019s fees In any action commenced pursuant to this subsection, the court, in its discretion, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee, not to exceed $3,000 in amount, as part of the costs, and the United States shall be liable for costs the same as a private person. (7) Requirements in certain States and local areas In the case of an alleged act or practice prohibited by this section which occurs in a State, or political subdivision of a State, which has a State or local law prohibiting such act or practice and establishing or authorizing a State or local authority to grant or seek relief from such act or practice or to institute criminal proceedings with respect thereto upon receiving notice thereof, no civil action may be brought hereunder before the expiration of 30 days after written notice of such alleged act or practice has been given to the appropriate State or local authority by registered mail or in person, provided that the court may stay proceedings in such civil action pending the termination of State or local enforcement proceedings. (f) Greater protection under State law This section shall not preempt any law of a State, the District of Columbia, a Tribal government, or a territory of the United States if the protections that such law affords to consumers are greater than the protections provided under this section. (g) Rulemaking The Secretary of the Treasury shall issue such rules as the Secretary determines are necessary to implement this section, which may include prescribing additional exceptions to the application of the requirements described in subsection (a). .\n##### (b) Clerical amendment\nThe table of contents for chapter 51 of title 31, United States Code, is amended by inserting after the item relating to section 5103 the following:\n5104. Retail businesses prohibited from refusing cash payments. .",
      "versionDate": "2025-02-07",
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
        "updateDate": "2025-03-11T18:29:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1138",
          "measure-number": "1138",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1138v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Payment Choice Act of 2025</strong><strong></strong></p><p>This bill requires retail businesses to accept cash as a form of payment for on-site sales of $500 or less and it prohibits them from charging cash-paying customers a higher price compared to customers not paying with cash. Businesses covered by this bill are those engaged in the business of selling or offering goods or services at retail to the public that accept in-person payments at a physical location.</p><p>The bill establishes exceptions for this requirement, including by allowing a business to provide a device to provide prepaid cards on site for customers to use as payment. Among other requirements, such a card must not have a fee associated with its use and must not require a minimum payment of more than $1.</p><p>The bill provides for enforcement through preventative relief, damages, and civil penalties.</p>"
        },
        "title": "Payment Choice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1138.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Payment Choice Act of 2025</strong><strong></strong></p><p>This bill requires retail businesses to accept cash as a form of payment for on-site sales of $500 or less and it prohibits them from charging cash-paying customers a higher price compared to customers not paying with cash. Businesses covered by this bill are those engaged in the business of selling or offering goods or services at retail to the public that accept in-person payments at a physical location.</p><p>The bill establishes exceptions for this requirement, including by allowing a business to provide a device to provide prepaid cards on site for customers to use as payment. Among other requirements, such a card must not have a fee associated with its use and must not require a minimum payment of more than $1.</p><p>The bill provides for enforcement through preventative relief, damages, and civil penalties.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hr1138"
    },
    "title": "Payment Choice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Payment Choice Act of 2025</strong><strong></strong></p><p>This bill requires retail businesses to accept cash as a form of payment for on-site sales of $500 or less and it prohibits them from charging cash-paying customers a higher price compared to customers not paying with cash. Businesses covered by this bill are those engaged in the business of selling or offering goods or services at retail to the public that accept in-person payments at a physical location.</p><p>The bill establishes exceptions for this requirement, including by allowing a business to provide a device to provide prepaid cards on site for customers to use as payment. Among other requirements, such a card must not have a fee associated with its use and must not require a minimum payment of more than $1.</p><p>The bill provides for enforcement through preventative relief, damages, and civil penalties.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hr1138"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1138ih.xml"
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
      "title": "Payment Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Payment Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that United States currency is treated as legal tender to be accepted as payment for purchases of goods and services at brick-and-mortar businesses throughout the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:33Z"
    }
  ]
}
```
