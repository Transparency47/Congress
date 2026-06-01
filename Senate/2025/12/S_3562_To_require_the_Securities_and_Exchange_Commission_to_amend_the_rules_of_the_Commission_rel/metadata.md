# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3562
- Title: Disclosing Investments in Foreign Adversaries Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3562
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-01-22T15:38:39Z
- Update date including text: 2026-01-22T15:38:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3562",
    "number": "3562",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Disclosing Investments in Foreign Adversaries Act of 2025",
    "type": "S",
    "updateDate": "2026-01-22T15:38:39Z",
    "updateDateIncludingText": "2026-01-22T15:38:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T17:36:25Z",
          "name": "Referred To"
        }
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3562is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3562\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Scott of Florida (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Securities and Exchange Commission to amend the rules of the Commission relating to disclosures by advisers of private funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disclosing Investments in Foreign Adversaries Act of 2025 .\n#### 2. Enhanced disclosure requirements for advisers of private funds\nSection 204 of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20134 ) is amended by adding at the end the following:\n(g) Enhanced disclosure requirements for advisers of private funds (1) Definitions In this subsection: (A) Country of concern The term country of concern \u2014 (i) has the meaning given the term covered nation in section 4872(f) of title 10, United States Code; and (ii) includes a jurisdiction that the Commission, in consultation with the Secretary of State and the Secretary of the Treasury, determines to be subject to the political and legal control of a covered nation, as defined in section 4872(f) of title 10, United States Code. (B) Covered investment adviser The term covered investment adviser means\u2014 (i) an investment adviser required to register with the Commission that, together with all related persons, has at least $150,000,000 in private fund assets under management; and (ii) an investment adviser relying on the exemption from registration provided under subsection (l) or (m) of section 203. (C) Private fund asset With respect to an investment adviser, the term private fund asset means an asset under management by the investment adviser that is attributable to a private fund. (D) Related person The term related person has the meaning given that term in the form described in section 279.1 of title 17, Code of Federal Regulations, as in effect on the date of enactment of this subsection. (2) Reporting requirements (A) In general Each covered investment adviser shall file an annual report with the Commission stating the total private fund assets in countries of concern attributable to the private funds advised by the covered investment adviser, which shall be broken down by the percentage of those assets in each country of concern. (B) Application For the purposes of subparagraph (A), the Commission shall determine whether a private fund asset is in a country of concern based on\u2014 (i) the amount of capital that is invested in an entity (including a subsidiary of an entity)\u2014 (I) that has a physical presence or employees in that country of concern; or (II) the plurality of the sales of which are from that country of concern; and (ii) the proportion of the total assets and liabilities of an entity described in clause (i) that are located in that country of concern. (3) Reporting by Commission (A) Publicly available reports Not later than 1 year after the date of enactment of this subsection, and not less frequently than annually thereafter, the Commission shall prepare and make publicly available a report containing a list of covered investment advisers that, for the period covered by the report, have disclosed to the Commission more than 0 private fund assets in at least 1 country of concern. (B) Additional requirements Each report prepared and made available by the Commission under subparagraph (A) shall\u2014 (i) be aggregated by a covered investment adviser; and (ii) include the percentage of private fund assets disclosed by a covered investment adviser, as applicable. .\n#### 3. Exempted transactions\nThe Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ) is amended by inserting after section 13A ( 15 U.S.C. 78m\u20131 ) the following:\n13B. Disclosure requirements relating to certain exempted transactions (a) Definitions In this section: (1) Beneficial owner The term beneficial owner means a person that is determined to be a beneficial owner under section 240.13d\u20133 of title 17, Code of Federal Regulations, or any successor regulation. (2) Country of concern The term country of concern \u2014 (A) has the meaning given the term covered nation in section 4872(f) of title 10, United States Code; and (B) includes a jurisdiction that the Commission, in consultation with the Secretary of State and the Secretary of the Treasury, determines to be subject to the political and legal control of a covered nation, as defined in section 4872(f) of title 10, United States Code. (3) Covered exempted transaction The term covered exempted transaction means an offer or sale of a security that is\u2014 (A) exempted under section 4 of the Securities Act of 1933 ( 15 U.S.C. 77d ); and (B) structured or intended to comply with\u2014 (i) section 230.506(b) of title 17, Code of Federal regulations, or any successor regulation; (ii) sections 230.901, 230.902, and 230.903 of title 17, Code of Federal Regulations, or any successor regulations; or (iii) section 230.144A of title 17, Code of Federal Regulations, or any successor regulation. (b) Requirement (1) In general Notwithstanding any other provision of law, in the case of an issuer that conducts a covered exempted transaction described in paragraph (2), that issuer shall provide to the Commission, at such time and in such manner as the Commission may prescribe, the following information: (A) The identity of the issuer. (B) The place of incorporation of the issuer. (C) Whether the issuer is associated with at least 1 consolidated entity, the plurality of the assets of which are in a country of concern. (D) Whether the issuer is associated with at least 1 consolidated entity that is incorporated in a country of concern. (E) The amount of securities sold pursuant to the covered exempted transaction and the net proceeds to the issuer. (F) The beneficial owners of the issuer. (G) The intended use of the proceeds from the covered exempted transaction, including each country in which the issuer intends to invest those proceeds, which shall be broken down by the percentage of net proceeds by industry within each such country. (H) The exemption the issuer relies on with respect to the covered exempted transaction. (2) Particular covered exempted transaction described A covered exempted transaction described in this paragraph is, with respect to the issuer offering or selling the security that is the subject of the covered exempted transaction, either of the following instances: (A) An offer or sale of securities in an amount that is not less than $25,000,000. (B) An offer or sale of a security such that the offer or sale, together with all covered exempted transactions by that issuer during the 1-year period preceding the date on which the issuer offers or sells the security, constitutes offers or sales in the aggregate of an amount that is not less than $50,000,000. (c) Authority To revise and promulgate rules, regulations, and forms The Commission shall, for the protection of investors and fair and orderly markets\u2014 (1) revise and issue such rules, regulations, and forms as may be necessary to carry out this section; and (2) issue rules to set conditions that limit the future use of covered exempted transactions for issuers that do not comply with the disclosure requirements of this section. (d) Applicability This section shall apply with respect to any covered exempted transaction that occurs on or after the date that is 1 year after the date of enactment of this section. (e) Reports The Commission shall, on a quarterly basis, prepare and make publicly available a report that includes all information submitted by an issuer under this section during the quarter covered by the report, if that issuer\u2014 (1) is\u2014 (A) incorporated in a country of concern; or (B) incorporated outside of a country of concern and is associated with at least 1 consolidated entity\u2014 (i) the plurality of the assets of which are in a country of concern; or (ii) that is incorporated in a country of concern; or (2) discloses in a filing made pursuant to this section that the issuer intends to invest the proceeds from a covered exempted transaction in a country of concern. .",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-22T15:38:39Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3562is.xml"
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
      "title": "Disclosing Investments in Foreign Adversaries Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disclosing Investments in Foreign Adversaries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Securities and Exchange Commission to amend the rules of the Commission relating to disclosures by advisers of private funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:30Z"
    }
  ]
}
```
