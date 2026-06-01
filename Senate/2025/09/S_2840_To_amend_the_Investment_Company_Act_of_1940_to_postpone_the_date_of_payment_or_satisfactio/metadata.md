# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2840?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2840
- Title: Financial Exploitation Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2840
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2840",
    "number": "2840",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Financial Exploitation Prevention Act of 2025",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
        "item": [
          {
            "date": "2025-09-17T19:14:02Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-17T19:14:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "AZ"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "ME"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2840is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2840\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Hagerty (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Investment Company Act of 1940 to postpone the date of payment or satisfaction upon redemption of certain securities in the case of the financial exploitation of specified adults, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Exploitation Prevention Act of 2025 .\n#### 2. Redemption of certain securities postponed\n##### (a) In general\nSection 22 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u201322 ) is amended by adding at the end the following:\n(h) Requirements with respect to non-Institutional direct at-Fund accounts (1) Election (A) In general A registered open-end investment company and a transfer agent described in paragraph (2) may elect to comply with the requirements under paragraph (2) and subsection (i) by notifying the Commission of that election. (B) Effect of election Paragraph (2) and subsection (i) shall only apply to a registered open-end investment company and a transfer agent that have made an election under subparagraph (A). (2) Requirements In the case of a customer who is a holder of a non-institutional account held directly with a registered open-end investment company and serviced by a transfer agent (commonly known as a direct-at-fund account ), the company and transfer agent shall\u2014 (A) request from that customer the name and contact information of at least 1 individual who\u2014 (i) is, at the time of that request, an adult; and (ii) may be contacted with respect to that account; (B) document and retain the information received under subparagraph (A); and (C) disclose to that customer in writing (including through electronic delivery) that such company or transfer agent may contact an individual specified under subparagraph (A) with respect to the account of that customer to\u2014 (i) address possible financial exploitation of that customer; (ii) confirm the contact information or health status of that customer; or (iii) identify any legal guardian, executor, trustee, or holder of a power of attorney with respect to the customer. (i) Redemption of certain securities postponed (1) In general Notwithstanding subsection (e), a registered open-end investment company or a transfer agent acting on behalf of such a company may postpone the date of payment or satisfaction upon redemption of any redeemable security in accordance with its terms for more than seven days after the tender of such security to such company or its agent designated for that purpose for redemption if such company or agent reasonably believes that\u2014 (A) that redemption is requested by a security holder who is a specified adult; and (B) financial exploitation has occurred, is occurring, or has been attempted with respect to that redemption. (2) Duration (A) In general Except as provided in subparagraphs (B) and (C), a registered open-end investment company or a transfer agent acting on behalf of such company may postpone the date of payment or satisfaction upon redemption of a redeemable security under paragraph (1) for a period of not more than 15 business days. (B) Extension upon determination of exploitation The period described in subparagraph (A) may be extended by an additional 10 business days if the registered open-end investment company or a transfer agent acting on behalf of such a company\u2014 (i) reasonably believes that\u2014 (I) the redemption is requested by a security holder who is a specified adult; and (II) financial exploitation has occurred, is occurring, or has been attempted with respect to such redemption; (ii) subject to subparagraph (D), not later than 2 days after making a determination under clause (i), notifies the individuals specified by that security holder under subsection (h)(2)(A) in writing (including through electronic delivery) of the extension of the period described in subparagraph (A) under this subparagraph and the reason for that extension; (iii) initiates an internal review of the facts and circumstances relating to the determination under clause (i); (iv) holds amounts relating to the delayed payment or satisfaction upon redemption of the redeemable security in a demand deposit account; and (v) documents and retains records related to carrying out clause (iv) and includes those records in the first required account statement of the security holder provided after the date on which the determination is made under clause (i). (C) Extension by government A State regulator, administrative agency of competent jurisdiction, or court of competent jurisdiction may extend the period described in subparagraph (A). (D) Notification (i) Exception Subparagraph (B)(ii) shall not apply if a registered open-end investment company or transfer agent acting on behalf of such a company reasonably believes that an individual required to be notified under that subparagraph is, has been, or will subject the security holder who identified that individual under subsection (h)(2)(A) to financial exploitation. (ii) Reasonable efforts An open-end investment company or transfer agent acting on behalf of such a company shall be considered in compliance with subparagraph (B)(ii) if that company or transfer agent makes a reasonable effort to contact the individuals specified by a security holder under subsection (h)(2)(A). (E) Internal procedures An open-end investment company or transfer agent acting on behalf of such a company shall establish procedures to carry out the requirements under this subsection, including procedures\u2014 (i) relating to the identification and reporting of matters relating to the financial exploitation of specified adults; (ii) to determine whether to release or reinvest delayed redemption proceeds, taking into account the facts and circumstances of each case, should the internal review under subparagraph (B)(iii) support the reasonable belief described in subparagraph (B)(i); (iii) identifying each employee of the company or transfer agent with authority to establish, extend, or terminate a period described in paragraph (1) or subparagraph (A); (iv) in the case of a transfer agent, that are reasonably designed to ensure that the employees of the transfer agent comply with this subsection; and (v) in the case of an open-end investment company, establishing periodic reporting requirements under which a transfer agent acting on behalf of the company shall notify the company of\u2014 (I) each extension under subparagraph (B) authorized by the transfer agent; (II) each finding by the transfer agent under subparagraph (B)(i); (III) each notification under subparagraph (B)(ii) carried out by the transfer agent; and (IV) the results of each internal review initiated by the transfer agent under subparagraph (B)(iii). (F) Information included in certain statements An open-end investment company shall include in each prospectus or statement of additional information a notification that the company or a transfer agent acting on behalf of the company may postpone redemption of certain securities under this subsection. (G) Record retention An open-end investment company or transfer agent acting on behalf of such a company shall\u2014 (i) document and retain records of\u2014 (I) each postponement of redemption under subparagraphs (A), (B), and (C); (II) each finding under subparagraph (B)(i); (III) the name and position of each employee described in subparagraph (E)(iii); (IV) each notification carried out under subparagraph (B)(ii); and (V) the results of each internal review initiated under subparagraph (B)(iii); and (ii) make the records described in clause (i) available to the Commission at the request of the Commission. (3) Specified adult defined In this subsection, the term specified adult means an individual who\u2014 (A) is not younger than 65 years of age; or (B) is not younger than 18 years of age and who a registered open-end investment company or a transfer agent acting on behalf of such a company reasonably believes has a mental or physical impairment that renders the individual unable to protect the interests of the individual. .\n##### (b) Recommendations\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Securities and Exchange Commission, in consultation with the entities specified in paragraph (2), shall submit to Congress a report that includes recommendations regarding the regulatory and legislative changes necessary to address the financial exploitation of security holders who are specified adults (as defined in subsection (i)(3) of section 22 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u201322 ), as added by this section).\n**(2) Consultation**\nThe entities specified in this paragraph are as follows:\n**(A)**\nThe Commodity Futures Trading Commission.\n**(B)**\nThe Director of the Bureau of Consumer Financial Protection.\n**(C)**\nThe Financial Industry Regulatory Authority.\n**(D)**\nThe North American Securities Administrators Association.\n**(E)**\nThe Board of Governors of the Federal Reserve System.\n**(F)**\nThe Comptroller of the Currency.\n**(G)**\nThe Federal Deposit Insurance Corporation.",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-11-04",
        "text": "Placed on the Union Calendar, Calendar No. 313."
      },
      "number": "2478",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Financial Exploitation Prevention Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-11-18T18:53:46Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2840is.xml"
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
      "title": "Financial Exploitation Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Exploitation Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-02T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Investment Company Act of 1940 to postpone the date of payment or satisfaction upon redemption of certain securities in the case of the financial exploitation of specified adults, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-02T04:18:14Z"
    }
  ]
}
```
