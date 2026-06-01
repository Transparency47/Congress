# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2713
- Title: MAIN Event Ticketing Act
- Congress: 119
- Bill type: HR
- Bill number: 2713
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-04-09T14:15:02Z
- Update date including text: 2026-04-09T14:15:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2713",
    "number": "2713",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "MAIN Event Ticketing Act",
    "type": "HR",
    "updateDate": "2026-04-09T14:15:02Z",
    "updateDateIncludingText": "2026-04-09T14:15:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2713ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2713\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mrs. Harshbarger (for herself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve online ticket sales and protect consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mitigating Automated Internet Networks for Event Ticketing Act or the MAIN Event Ticketing Act .\n#### 2. Strengthening the BOTS Act\n##### (a) In general\nSection 2 of the Better Online Ticket Sales Act of 2016 ( 15 U.S.C. 45c ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(C) to use or cause to be used an application that performs automated tasks to purchase event tickets from an internet website or online service in circumvention of posted online ticket purchasing order rules of the internet website or online service, including a software application that circumvents an access control system, security measure, or other technological control or measure. ;\n**(2)**\nby redesignating subsections (b) and (c) as subsections (c) and (d), respectively;\n**(3)**\nby inserting after subsection (a) the following new subsection:\n(b) Requiring online ticket issuers To put in place site policies and establish safeguards To protect site security (1) Requirement to enforce site policies Each ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets shall ensure that such website or service has in place an access control system, security measure, or other technological control or measure to enforce posted event ticket purchasing limits. (2) Requirement to establish site security safeguards (A) In general Each ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets shall establish, implement, and maintain reasonable administrative, technical, and physical safeguards to protect the security, confidentiality, integrity, or availability of the website or service. (B) Considerations In establishing the safeguards described in subparagraph (A), each ticket issuer described in such paragraph shall consider\u2014 (i) the administrative, technical, and physical safeguards that are appropriate to the size and complexity of the ticket issuer; (ii) the nature and scope of the activities of the ticket issuer; (iii) the sensitivity of any customer information at issue; and (iv) the range of security risks and vulnerabilities that are reasonably foreseeable or known to the ticket issuer. (C) Third parties and service providers (i) In general Where applicable, a ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets shall implement and maintain procedures to require that any third party or service provider that performs services with respect to the sale of event tickets or has access to data regarding event ticket purchasing on the website or service maintains reasonable administrative, technical, and physical safeguards to protect the security and integrity of the website or service and that data. (ii) Oversight procedure requirements The procedures implemented and maintained by a ticket issuer in accordance with clause (i) shall include the following: (I) Taking reasonable steps to select and retain service providers that are capable of maintaining appropriate safeguards for the customer information at issue. (II) Requiring service providers by contract to implement and maintain adequate safeguards. (III) Periodically assessing service providers based on the risk they present and the continued adequacy of their safeguards. (D) Updates A ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets shall regularly evaluate and make adjustments to the safeguards described in subparagraph (A) in light of any material changes in technology, internal or external threats to system security, confidentiality, integrity, and availability, and the changing business arrangements or operations of the ticket issuer. (3) Requirement to report incidents of circumvention; consumer complaints (A) In general A ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets shall report to the Commission any incidents of circumvention of which the ticket issuer has actual knowledge. (B) Consumer complaint website Not later than 180 days after the date of enactment of the Mitigating Automated Internet Networks for Event Ticketing Act , the Commission shall create a publicly available website (or modify an existing publicly available website of the Commission) to allow individuals to report violations of this subsection to the Commission. (C) Reporting timeline and process (i) Timeline A ticket issuer shall report known incidents of circumvention within a reasonable period of time after the incident of circumvention is discovered by the ticket issuer, and in no case later than 30 days after an incident of circumvention is discovered by the ticket issuer. (ii) Automated submission The Commission may establish a reporting mechanism to provide for the automatic submission of reports required under this subsection. (iii) Coordination with state attorneys general The Commission shall\u2014 (I) share reports received from ticket issuers under subparagraph (A) with State attorneys general as appropriate; and (II) share consumer complaints submitted through the website established under subparagraph (B) with State attorneys general as appropriate. (4) Duty to address causes of circumvention A ticket issuer that owns or operates an internet website or online service that facilitates or executes the sale of event tickets must take reasonable steps to improve its access control systems, security measures, and other technological controls or measures to address any incidents of circumvention of which the ticket issuer has actual knowledge. (5) FTC guidance Not later than 1 year after the date of enactment of the Mitigating Automated Internet Networks for Event Ticketing Act , the Commission shall publish guidance for ticket issuers on compliance with the requirements of this subsection. ;\n**(4)**\nin subsection (c), as redesignated by paragraph (1) of this subsection\u2014\n**(A)**\nby striking subsection (a) each place it appears and inserting subsection (a) or (b) ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking The Commission and inserting Except as provided in paragraph (3), the Commission ; and\n**(ii)**\nin subparagraph (B), by striking Any person and inserting Subject to paragraph (3), any person ; and\n**(C)**\nby adding at the end the following new paragraphs:\n(3) Civil action (A) In general If the Commission has reason to believe that any person has committed a violation of subsection (a) or (b), the Commission may bring a civil action in an appropriate district court of the United States to\u2014 (i) recover a civil penalty under paragraph (4); and (ii) seek other appropriate relief, including injunctive relief and other equitable relief. (B) Litigation authority Except as otherwise provided in section 16(a)(3) of the Federal Trade Commission Act ( 15 U.S.C. 56(a)(3) ), the Commission shall have exclusive authority to commence or defend, and supervise the litigation of, any civil action authorized under this paragraph and any appeal of such action in its own name by any of its attorneys designated by it for such purpose, unless the Commission authorizes the Attorney General to do so. The Commission shall inform the Attorney General of the exercise of such authority and such exercise shall not preclude the Attorney General from intervening on behalf of the United States in such action and any appeal of such action as may be otherwise provided by law. (C) Rule of construction Any civil penalty or relief sought through a civil action under this paragraph shall be in addition to other penalties and relief as may be prescribed by law. (4) Civil penalties (A) In general Any person who violates subsection (a) or (b) shall be liable for\u2014 (i) a civil penalty of not less than $10,000 for each day during which the violation occurs or continues to occur; and (ii) an additional civil penalty of not less than $1,000 per violation. (B) Enhanced civil penalty for intentional violations In addition to the civil penalties under subparagraph (A), a person that intentionally violates subsection (a) or (b) shall be liable for a civil penalty of not less than $10,000 per violation. ;\n**(5)**\nin subsection (d), as redesignated by paragraph (1) of this subsection, by striking subsection (a) each place it appears and inserting subsection (a) or (b) ; and\n**(6)**\nby adding at the end the following new subsections:\n(e) Law enforcement coordination (1) In general The Federal Bureau of Investigation, the Department of Justice, and other relevant State or local law enforcement officials shall coordinate as appropriate with the Commission to share information about known instances of cyberattacks on security measures, access control systems, or other technological controls or measures on an internet website or online service that are used by ticket issuers to enforce posted event ticket purchasing limits or to maintain the integrity of posted online ticket purchasing order rules. Such coordination may include providing information about ongoing investigations but may exclude classified information or information that could compromise a law enforcement or national security effort, as appropriate. (2) Cyberattack defined In this paragraph, the term cyberattack means an attack, via cyberspace, targeting an enterprise\u2019s use of cyberspace for the purpose of\u2014 (A) disrupting, disabling, destroying, or maliciously controlling a computing environment or computing infrastructure; or (B) destroying the integrity of data or stealing controlled information. (f) Congressional report Not later than 1 year after the date of enactment of this paragraph, the Commission shall report to Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives on the status of enforcement actions taken pursuant to this Act, as well as any identified limitations to the Commission\u2019s ability to pursue incidents of circumvention described in subsection (a)(1)(A). .\n##### (b) Additional definition\nSection 3 of the Better Online Ticket Sales Act of 2016 ( 15 U.S.C. 45c note) is amended by adding at the end the following new paragraph:\n(4) Circumvention The term circumvention means the act of avoiding, bypassing, removing, deactivating, or otherwise impairing an access control system, security measure, safeguard, or other technological control or measure described in section 2(b)(1). .",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-09-02",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 144."
      },
      "number": "196",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MAIN Event Ticketing Act",
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
        "name": "Commerce",
        "updateDate": "2025-05-15T15:50:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
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
          "measure-id": "id119hr2713",
          "measure-number": "2713",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2713v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mitigating Automated Internet Networks for Event Ticketing Act or the MAIN Event Ticketing Act</strong></p><p>This bill expands measures to protect the security and integrity of online ticket sales.</p><p>Specifically, the bill prohibits the use of applications that perform automated tasks to purchase event tickets from online ticket sellers in circumvention of the seller's posted ticket purchasing order rules. This includes using software applications that circumvent access control systems or security measures.</p><p>In addition, online ticket sellers must establish, implement, and maintain reasonable administrative, technical, and physical safeguards to protect the security, confidentiality, integrity, or availability of the seller's website or service.\u00a0</p><p>Further, online ticket sellers must report known incidents of circumvention to the Federal Trade Commission and take reasonable steps to address any such incidents.</p><p>The bill establishes civil penalties for violations of the provisions\u00a0of this bill (and related prohibitions under current law) and authorizes the commission to bring civil actions for such violations.</p><p>Federal, state, and local law enforcement agencies must coordinate as appropriate with the commission to share information about known instances of cyberattacks against the websites or online services used by ticket sellers.</p><p>The commission must report to Congress on the status of enforcement actions taken under this bill.</p>"
        },
        "title": "MAIN Event Ticketing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2713.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mitigating Automated Internet Networks for Event Ticketing Act or the MAIN Event Ticketing Act</strong></p><p>This bill expands measures to protect the security and integrity of online ticket sales.</p><p>Specifically, the bill prohibits the use of applications that perform automated tasks to purchase event tickets from online ticket sellers in circumvention of the seller's posted ticket purchasing order rules. This includes using software applications that circumvent access control systems or security measures.</p><p>In addition, online ticket sellers must establish, implement, and maintain reasonable administrative, technical, and physical safeguards to protect the security, confidentiality, integrity, or availability of the seller's website or service.\u00a0</p><p>Further, online ticket sellers must report known incidents of circumvention to the Federal Trade Commission and take reasonable steps to address any such incidents.</p><p>The bill establishes civil penalties for violations of the provisions\u00a0of this bill (and related prohibitions under current law) and authorizes the commission to bring civil actions for such violations.</p><p>Federal, state, and local law enforcement agencies must coordinate as appropriate with the commission to share information about known instances of cyberattacks against the websites or online services used by ticket sellers.</p><p>The commission must report to Congress on the status of enforcement actions taken under this bill.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr2713"
    },
    "title": "MAIN Event Ticketing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mitigating Automated Internet Networks for Event Ticketing Act or the MAIN Event Ticketing Act</strong></p><p>This bill expands measures to protect the security and integrity of online ticket sales.</p><p>Specifically, the bill prohibits the use of applications that perform automated tasks to purchase event tickets from online ticket sellers in circumvention of the seller's posted ticket purchasing order rules. This includes using software applications that circumvent access control systems or security measures.</p><p>In addition, online ticket sellers must establish, implement, and maintain reasonable administrative, technical, and physical safeguards to protect the security, confidentiality, integrity, or availability of the seller's website or service.\u00a0</p><p>Further, online ticket sellers must report known incidents of circumvention to the Federal Trade Commission and take reasonable steps to address any such incidents.</p><p>The bill establishes civil penalties for violations of the provisions\u00a0of this bill (and related prohibitions under current law) and authorizes the commission to bring civil actions for such violations.</p><p>Federal, state, and local law enforcement agencies must coordinate as appropriate with the commission to share information about known instances of cyberattacks against the websites or online services used by ticket sellers.</p><p>The commission must report to Congress on the status of enforcement actions taken under this bill.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr2713"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2713ih.xml"
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
      "title": "MAIN Event Ticketing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T09:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAIN Event Ticketing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mitigating Automated Internet Networks for Event Ticketing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve online ticket sales and protect consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T09:33:16Z"
    }
  ]
}
```
