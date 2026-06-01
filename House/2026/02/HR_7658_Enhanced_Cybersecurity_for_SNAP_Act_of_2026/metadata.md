# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7658
- Title: Enhanced Cybersecurity for SNAP Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7658
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-05-22T08:08:50Z
- Update date including text: 2026-05-22T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7658",
    "number": "7658",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Enhanced Cybersecurity for SNAP Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:50Z",
    "updateDateIncludingText": "2026-05-22T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7658ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7658\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Mr. Goldman of New York (for himself, Mr. Lawler , Mr. Smith of Washington , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to require the promulgation of cybersecurity and digital service regulations relating to the use of EBT cards under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhanced Cybersecurity for SNAP Act of 2026 .\n#### 2. Enhanced cybersecurity for EBT cards\nSection 7(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h) ) is amended by adding at the end the following:\n(15) Cybersecurity of EBT cards (A) Definitions In this paragraph: (i) Chip-enabled (I) In general The term chip-enabled , with respect to a payment card, means a payment card that uses industry standard secure payment technology, as identified by the Administrator of the Food and Nutrition Service in consultation with the Secretary of the Treasury and the Director of the National Institute of Standards and Technology, that\u2014 (aa) provides for secure card-based payment; and (bb) is resistant to cloning. (II) Chip card technology The Administrator of the Food and Nutrition Service, in consultation with the Secretary of the Treasury and the Accredited Standards Committee X9, shall consider whether the secure payment technology described in subclause (I) should meet the industry standards for contact and contactless payments. (ii) Mobile friendly The term \u2018mobile friendly\u2019 has the meaning given the term in section 3559(b) of title 44, United States Code. (iii) NIST PIN and password standards The term NIST PIN and password standards means the PIN and password standards described in Special Publication 800\u201363B entitled Digital Identity Guidelines (or a successor document) of the National Institute of Standards and Technology. (iv) PIN The term PIN has the meaning given the term personal identification number (PIN) in section 271.2 of title 7, Code of Federal Regulations (or successor regulations). (B) Regulations (i) In general Not later than 2 years after the date of enactment of this paragraph, the Secretary shall promulgate, and every 5 years thereafter, the Secretary shall review and update as necessary, cybersecurity and digital service regulations relating to EBT cards and mobile technologies under the supplemental nutrition assistance program, including, at a minimum, to ensure that cybersecurity measures for EBT cards and mobile technologies keep pace with security safeguards used by the private sector and required by Federal agencies for credit, debit, and other payment cards and mobile technologies. (ii) Requirements The Secretary shall ensure that the cybersecurity and digital service regulations described in clause (i) require the following: (I) (aa) Each State shall operate the user interfaces listed on the list of required user interfaces maintained by the Secretary under item (dd)(AA), in accordance with this subclause, 1 or more user interfaces of which households in the State may, at the election of the applicable household, use to manage the EBT account of the applicable household. (bb) (AA) A State may operate other user interfaces under item (aa) in addition to the required user interfaces on the list maintained by the Secretary under item (dd)(AA). (BB) Any web-based online portal operated by a State as a user interface shall be mobile friendly. (cc) Each user interface offered by a State under items (aa) and (bb), as applicable, shall\u2014 (AA) provide information in each language in which the State agency is required to make material available pursuant to section 272.4(b) of title 7, Code of Federal Regulations (or successor regulations); (BB) be available to households at least 99 percent of the time; and (CC) include any other features required by the Secretary. (dd) (AA) The Secretary shall maintain a list of required user interfaces for purposes of item (aa), which may include a web-based online portal and a mobile application. (BB) The list under subitem (AA) shall include an application programming interface through which at least 1 user interface offered by a State under item (aa) allows households to delegate access to some or all account features identified by the Secretary to third-party provided software. No fee shall be charged to any party for the use of that application programming interface. (CC) During the 10-year period following the date on which the regulations promulgated pursuant to clause (i) become final, unless the Secretary extends that period, the Secretary shall maintain on the list under subitem (AA) the following user interfaces: text message, voice telephone service, and a nondigital user interface that does not require the use of a phone or computer by the household. (II) (aa) Each State shall provide households on an opt-in basis\u2014 (AA) through each digital user interface offered under subclause (I), timely electronic notice of transactions using the EBT account of the household; and (BB) through each user interface offered under subclause (I), access to, including the ability to search, historical transactions for not less than the preceding 12 months. (bb) Transaction information under subitems (AA) and (BB) of item (aa) shall include the amount of the transaction, the merchant for the transaction, the city and State of the merchant for an in-person transaction, and the delivery address or collection address for an online transaction. (cc) Each State shall offer households the ability, through each user interface offered under subclause (I), to report a fraudulent transaction to the State. (dd) A State shall not require a household to respond to or acknowledge a notice of transaction delivered pursuant to item (aa)(AA). (ee) A State shall notify any household that has reported an instance of EBT card skimming or fraud, or is otherwise identified as being a victim of EBT card skimming or fraud, of any State or Federal funds that may be reimbursed if the household experiences fraud again. (III) Each State shall provide households issued an EBT card the ability, through each user interface offered under subclause (I) to check the enrollment status of the household, including the date on which the household is required to apply for recertification. (IV) Not later than 2 years after the date on which the regulations promulgated pursuant to clause (i) become final, States shall begin issuing chip-enabled EBT cards. (V) Not later than 4 years after the date on which the regulations promulgated pursuant to clause (i) become final, States may not issue new EBT cards with magnetic stripes. (VI) Not later than 5 years after the date on which the regulations promulgated pursuant to clause (i) become final, States shall be required to reissue any existing valid EBT cards with magnetic stripes as chip-enabled EBT cards without magnetic stripes. (VII) In the case of a chip-enabled EBT card reissued pursuant to any of subclauses (IV) through (VI), absent suspicion of fraud, as applicable, a State shall\u2014 (aa) reissue a new chip-enabled EBT card; and (bb) deactivate the current chip-enabled EBT card on the date that is the earlier of\u2014 (AA) the date on which the new chip-enabled EBT card is activated; and (BB) 60 days after the date on which the new chip-enabled EBT card is sent to the household. (iii) Sunset for requirement to use chip technology Under the cybersecurity regulations described in clause (i), all EBT cards, except EBT cards issued to victims of a disaster pursuant to section 5(h) or solely for benefits under the summer electronic benefits transfer for children program established under section 13A of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1762 ), issued during the 5-year period following the deadline for carrying out clause (ii)(VI) shall be chip-enabled, unless the Secretary extends that period. (iv) Rule of construction The cybersecurity and digital service regulations described in clause (i) shall supersede any regulations promulgated under paragraph (2) of section 501(a) of division HH of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 2016a(a) ) (as in effect on the day before the date of enactment of the Enhanced Cybersecurity for SNAP Act of 2026 ). (C) Reimbursements Each State upgrading EBT cards to comply with the regulations promulgated under subparagraph (B)(i) shall receive reimbursement from the Secretary in an amount determined by the Secretary to cover all reasonable costs incurred by the State, including\u2014 (i) the 1-time up-front costs paid by the State to card vendors; (ii) the additional annual fees associated with chip-enabled cards paid by States to card vendors; and (iii) postage or other delivery-related costs. (D) Prohibition on password and PIN requirements inconsistent with Federal cybersecurity standards Beginning 60 days after the date of enactment of this paragraph, a State agency may not require, with respect to a PIN for use of an EBT card or a password for access to an online account or mobile application managing the EBT card\u2014 (i) that the PIN or password be periodically changed in circumstances that are prohibited by the NIST PIN and password standards; or (ii) that the password meet complexity requirements that are prohibited by the NIST PIN and password standards. (E) Grant program for chip-enabled EBT cards (i) Definitions In this subparagraph: (I) Administering entity The term administering entity means an entity awarded a grant under clause (ii) to provide subgrants to eligible entities. (II) Eligible entity The term eligible entity means\u2014 (aa) an entity described in paragraph (1) or (3) of section 3(o) that\u2014 (AA) is authorized to participate in the supplemental nutrition assistance program under section 9; (BB) does not have payment terminals that accept chip-enabled EBT cards; and (CC) is located in an area with limited grocery access, as determined by the Secretary; and (bb) an entity described in paragraph (2), (4), or (5) of section 3(o) that meets the requirements described in subitems (AA) and (BB) of item (aa). (ii) Grants The Secretary shall establish a grant program to award a grant to an administering entity to provide subgrants to eligible entities to upgrade to chip-compatible payment terminals that support contact and contactless payment card technology. (F) Data collection The Secretary shall\u2014 (i) collect, and publish on the website of the Department of Agriculture, data on\u2014 (I) the length of time each user interface offered by each State pursuant to subparagraph (B)(ii)(I) was unavailable for use, including due to technical problems or maintenance needs; and (II) cybersecurity measures adopted for EBT cards in each State; and (ii) maintain and annually update the data collected under clause (i) to support States in implementing any regulations promulgated pursuant to subparagraph (B)(i). (G) Public report (i) In general Not later than 1 year after the date of enactment of this paragraph, and every 2 years thereafter, the Secretary shall submit to the Committees on Appropriations and Agriculture, Nutrition, and Forestry of the Senate and the Committees on Appropriations and Agriculture of the House of Representatives, and make publicly available on the website of the Department of Agriculture, a report that\u2014 (I) identifies trends relating to the theft of benefits, including the frequency of theft of benefits, the locations at which EBT cards are compromised, and the method by which EBT cards are compromised; (II) evaluates the effectiveness of existing cybersecurity regulations for the supplemental nutrition assistance program, including identifying ineffective measures and the compliance burden borne by individual benefit recipients; (III) describes the efforts of States\u2014 (aa) to update cybersecurity measures for EBT cards; and (bb) to reimburse stolen benefits; and (IV) examines usability issues of EBT cards, including issues that present barriers to households using benefits or affect fraud prevention goals. (ii) Restricted annex The report under clause (i) may include a nonpublicly available annex containing classified or law enforcement-sensitive information and any identifying merchant information. .\n#### 3. Online transaction security\nSection 7(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h) ) (as amended by section 2) is amended by adding at the end the following:\n(16) Online transaction security (A) In general In promulgating and updating, as necessary, the regulations under paragraph (15)(B)(i), the Secretary shall, with respect to online transactions using EBT cards (or any successor financial product used for a substantially similar purpose)\u2014 (i) require security measures that\u2014 (I) are effective in detecting and preventing theft of benefits through online transactions, including the theft of data from online merchants that may compromise the ability of a household to use benefits in transactions with other merchants, either online or in-person; and (II) prevent sensitive data from being stolen during online transactions and securely manage sensitive data generated by online transactions, including through cybersecurity enhancements for online retailers; (ii) establish standard reporting methods for States to collect and share data with the Secretary on the scope of benefits and data being stolen through online transactions; and (iii) in carrying out clauses (i) and (ii), take into consideration the feasibility of cost, availability, and implementation for States. (B) Consultation In carrying out subparagraph (A), the Secretary shall consult with the Director of the Administration for Children and Families, the Attorney General of the United States, State agencies, retail food stores, and EBT contractors\u2014 (i) on the measures, methods, and considerations under that subparagraph; and (ii) to determine\u2014 (I) how benefits are being stolen and sensitive data is being compromised through online transactions; and (II) how those stolen benefits and data are being used. (C) Report (i) In general Not later than 3 years after the date of enactment of this paragraph, and every 2 years thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that includes\u2014 (I) to the maximum extent practicable, information on the frequency of theft of benefits, the number of reported thefts from online transactions, the amount of benefits stolen through online transactions, and the online retailers most commonly compromised; (II) a description of the measures and methods developed, and considerations taken, under subparagraph (A); (III) the determinations made under subparagraph (B)(ii); and (IV) recommendations on how to consistently detect, track, report, and prevent theft of benefits, including the theft of data described in subparagraph (A)(i)(I). (ii) Confidential annex The report under clause (i) may include a nonpublicly available confidential annex containing any identifying merchant information. .\n#### 4. Ensuring no loss of access to benefits due to EBT card damage, loss, or fraud\nSection 7(h)(7) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h)(7) ) is amended\u2014\n**(1)**\nby striking Regulations and inserting the following:\n(A) In general Regulations ; and\n**(2)**\nby adding at the end the following:\n(B) Ensuring no loss of access to benefits due to EBT card damage, loss, or fraud Not later than 180 days after the date of enactment of the Enhanced Cybersecurity for SNAP Act of 2026 , the Secretary shall promulgate regulations requiring the following: (i) If an EBT card is damaged, no longer functions properly, is stolen, or is frozen due to fraud, the applicable State shall take the necessary steps to ensure that the household receives a replacement card, either by mail or in person, as selected by the household, not later than 3 business days after the household submits to the State a request for a replacement EBT card. (ii) A State shall not require, but shall offer as an option, in-person collection of a new or replacement EBT card. .\n#### 5. No replacement fees for certain EBT cards\nSection 7(h)(8)(A) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h)(8)(A) ) is amended\u2014\n**(1)**\nby striking A State agency and inserting the following:\n(i) In general Except as provided in clause (ii), a State agency ; and\n**(2)**\nby adding at the end the following:\n(ii) Exceptions Beginning 60 days after the date of enactment of the Enhanced Cybersecurity for SNAP Act of 2026 , a State agency may not collect a charge under clause (i) if the replacement of the EBT card is due to\u2014 (I) the EBT card malfunctioning; (II) suspected or reported fraud relating to that EBT card by an individual outside of the household to which the EBT card belongs; (III) the expiration of the EBT card; or (IV) required replacement of the EBT card in compliance with regulations promulgated pursuant to paragraph (15)(B). .\n#### 6. Requirement for retailer use of chip-enabled payment terminals as a condition of SNAP participation\nSection 9(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2018(a) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby striking (2) The Secretary and inserting the following:\n(2) Regulations The Secretary ; and\n**(B)**\nby indenting the margins of subparagraphs (A) and (B) appropriately;\n**(2)**\nby indenting the margin of paragraph (3) appropriately; and\n**(3)**\nby adding at the end the following:\n(5) Chip-enabled payment terminals Beginning not later than 180 days after the date on which the regulations promulgated pursuant to section 7(h)(15)(B)(i) become final, the Secretary shall require retail food stores and wholesale food concerns seeking authorization or reauthorization to accept and redeem benefits under the supplemental nutrition assistance program to have a chip-enabled (as defined in section 7(h)(15)(A)) payment terminal at each retail location of the retail food store or wholesale food concern. .\n#### 7. Report on EBT cards issued in Puerto Rico\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture shall submit to the Committees on Appropriations and Agriculture, Nutrition, and Forestry of the Senate and the Committees on Appropriations and Agriculture of the House of Representatives, and make publicly available on the website of the Department of Agriculture, a report on the security of EBT cards (as defined in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 )) issued in the Commonwealth of Puerto Rico, including\u2014\n**(1)**\nthe resistance of those EBT cards to cloning; and\n**(2)**\nif appropriate, recommendations for improving the security of the electronic benefit transfer system against EBT card cloning-based fraud.\n##### (b) Restricted annex\nThe report under subsection (a) may include a nonpublicly available annex containing classified or law enforcement-sensitive information.\n#### 8. Conforming amendments\nSection 501 of division HH of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 2016a ), is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraphs (1) and (2);\n**(B)**\nby redesignating paragraphs (3) through (5) as paragraphs (1) through (3), respectively; and\n**(C)**\nin paragraph (3) (as so redesignated)\u2014\n**(i)**\nin subparagraph (B), by adding and at the end;\n**(ii)**\nby striking subparagraph (C); and\n**(iii)**\nby redesignating subparagraph (D) as subparagraph (C); and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)(vi), by striking measures and all that follows through (a)(1) and inserting measures ;\n**(ii)**\nin subparagraph (B), by adding and at the end;\n**(iii)**\nin subparagraph (C), by striking and at the end; and\n**(iv)**\nby striking subparagraph (D); and\n**(B)**\nin paragraph (3), by striking subsection (a)(3) and inserting subsection (a)(1) .",
      "versionDate": "2026-02-24",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3949",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Enhanced Cybersecurity for SNAP Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-13T21:49:45Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7658ih.xml"
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
      "title": "Enhanced Cybersecurity for SNAP Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhanced Cybersecurity for SNAP Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-11T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to require the promulgation of cybersecurity and digital service regulations relating to the use of EBT cards under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-11T03:18:22Z"
    }
  ]
}
```
