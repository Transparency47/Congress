# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2711
- Title: Go Pack Go Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2711
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-01-14T02:04:26Z
- Update date including text: 2026-01-14T02:04:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2711",
    "number": "2711",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Go Pack Go Act of 2025",
    "type": "S",
    "updateDate": "2026-01-14T02:04:26Z",
    "updateDateIncludingText": "2026-01-14T02:04:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T16:52:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2711is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2711\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Ms. Baldwin introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Communications Act of 1934 and title 17, United States Code, to provide greater access to in-State television broadcast programming for cable and satellite subscribers in certain counties.\n#### 1. Short title\nThis Act may be cited as the Go Pack Go Act of 2025 .\n#### 2. Carriage of network station signals in certain counties\n##### (a) In general\nPart I of title III of the Communications Act of 1934 ( 47 U.S.C. 301 et seq. ) is amended by adding at the end the following:\n346. Carriage of network station signals in certain counties (a) Definitions In this section\u2014 (1) the term cable operator has the meaning given the term in section 602; (2) the terms covered county and in-State, adjacent-market network station retransmission have the meanings given those terms in section 119(d) of title 17, United States Code, except that, in the case of a cable operator, any reference to a satellite carrier or a subscriber of a satellite carrier shall be considered to be a reference to a cable operator or a subscriber of a cable operator, respectively; (3) the term local market has the meaning given the term in section 122(j) of title 17, United States Code; (4) the term local network station means, with respect to a subscriber and a television network, the network station\u2014 (A) that is affiliated with the television network; and (B) within the local market in which the subscriber is located; and (5) the terms network station and satellite carrier have the meanings given those terms in section 119(d) of title 17, United States Code. (b) Subscriber election A cable operator or satellite carrier shall, at the election of a subscriber in a covered county with respect to a television network, provide to the subscriber\u2014 (1) retransmission of the signal of any local network station that the operator or carrier is required to retransmit to the subscriber without regard to this section; (2) an in-State, adjacent-market network station retransmission; or (3) both retransmissions described in paragraphs (1) and (2). (c) Relationship to local signal carriage requirements If a subscriber elects to receive only an in-State, adjacent-market network station retransmission under subsection (b)\u2014 (1) the provision of that retransmission to the subscriber shall be deemed to fulfill any obligation of the cable operator or satellite carrier to provide to the subscriber the signal of a local network station under section 338, 614, or 615; and (2) in the case of a satellite carrier that has been recognized as a qualified carrier under section 119(f) of title 17, United States Code, the provision of that retransmission instead of the signal of a local network station shall not affect the status of the satellite carrier as a qualified carrier for purposes of that section and section 342 of this Act. (d) Requirement subject to technical feasibility for satellite carriers A satellite carrier shall be required to provide a retransmission under subsection (b) only to the extent that such provision is technically feasible, as determined by the Commission. (e) Treatment of in-State, adjacent-Market network station retransmissions by cable operators (1) Retransmission consent exception Section 325(b) shall not apply to an in-State, adjacent-market network station retransmission by a cable operator to a subscriber residing in a covered county. (2) Deemed significantly viewed In the case of an in-State, adjacent-market network station retransmission by a cable operator to a subscriber residing in a covered county, the signal of the station shall be deemed to be significantly viewed in that county within the meaning of section 76.54 of title 47, Code of Federal Regulations, or any successor regulation. .\n##### (b) Treatment of in-State, adjacent-Market network station retransmissions by satellite carriers\nSection 339 of the Communications Act of 1934 ( 47 U.S.C. 339 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A), by adding at the end the following: In-State, adjacent-market network station retransmissions to subscribers residing in covered counties shall not count toward the limit set forth in this subparagraph. ; and\n**(B)**\nin paragraph (2), by adding at the end the following:\n(I) In-State, adjacent-market network station retransmissions Nothing in this paragraph shall apply to or affect in-State, adjacent-market network station retransmissions to subscribers residing in covered counties. ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (1) through (5) as paragraphs (3) through (7), respectively; and\n**(B)**\nby inserting before paragraph (3), as so redesignated, the following:\n(1) Covered county The term covered county has the meaning given the term in section 119(d) of title 17, United States Code. (2) In-State, adjacent-market network station retransmission The term in-State, adjacent-market network station retransmission has the meaning given the term in section 119(d) of title 17, United States Code. .\n##### (c) No effect on ability To receive significantly viewed signals\nSection 340(b)(3) of the Communications Act of 1934 ( 47 U.S.C. 340(b)(3) ) is amended by inserting before the period at the end the following: or to a subscriber who elects under section 346(b), with respect to the network with which the station whose signal is being retransmitted pursuant to this section is affiliated, to receive an in-State, adjacent-market network station retransmission (as defined in section 119(d) of title 17, United States Code) instead of the signal of a local network station (as defined in section 346) .\n#### 3. Availability of copyright license\n##### (a) Secondary transmissions of distant television programming by satellite\nSection 119 of title 17, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)(B)(i), by adding at the end the following: In-State, adjacent-market network station retransmissions to subscribers residing in covered counties shall not count toward the limit set forth in this clause. ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (10)\u2014\n**(i)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) with respect to an in-State, adjacent-market network station retransmission, is a subscriber residing in a covered county. ; and\n**(B)**\nby adding at the end the following:\n(17) In-State, adjacent-market network station retransmission The term in-State, adjacent-market network station retransmission means the secondary transmission by a satellite carrier of the primary transmission of any network station whose community of license is located\u2014 (A) in the State of a subscriber; and (B) in a local market that is adjacent to the local market of the subscriber. (18) Covered county The term covered county means, with respect to an in-State, adjacent-market network station retransmission to a subscriber, any county to which both of the following apply: (A) The county is one of the following counties in the State of Wisconsin: Ashland, Barron, Bayfield, Burnett, Douglas, Dunn, Florence, Iron, Pierce, Polk, Sawyer, St. Croix, or Washburn. (B) The county is not in the local market of any television broadcast station\u2014 (i) that is affiliated with the same network; and (ii) whose community of license is located in the State of the subscriber. .\n##### (b) Secondary transmissions of local television programming by satellite\nSection 122(a) of title 17, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)(A), by inserting after under paragraph (1) the following: (or in-State, adjacent-market network station retransmissions instead of secondary transmissions under that paragraph, in accordance with an election under section 346(b) of the Communications Act of 1934) ; and\n**(2)**\nin paragraph (3)(A), by inserting after under paragraph (1) the following: (or in-State, adjacent-market network station retransmissions instead of secondary transmissions under that paragraph, in accordance with an election under section 346(b) of the Communications Act of 1934) .",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-09-04",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5165",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Go Pack Go Act of 2025",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-22T15:49:43Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2711is.xml"
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
      "title": "Go Pack Go Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Go Pack Go Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Communications Act of 1934 and title 17, United States Code, to provide greater access to in-State television broadcast programming for cable and satellite subscribers in certain counties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:22Z"
    }
  ]
}
```
