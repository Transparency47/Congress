# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/273
- Title: Small Business Child Care Investment Act
- Congress: 119
- Bill type: S
- Bill number: 273
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-04-29T17:20:35Z
- Update date including text: 2026-04-29T17:20:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-05 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment favorably.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.
- 2025-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 9.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-05 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment favorably.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.
- 2025-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 9.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/273",
    "number": "273",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacklyn",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Small Business Child Care Investment Act",
    "type": "S",
    "updateDate": "2026-04-29T17:20:35Z",
    "updateDateIncludingText": "2026-04-29T17:20:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 9.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-28",
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
            "date": "2025-02-10T21:41:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T19:44:52Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-28T19:27:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "IA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "ID"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s273is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 273\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Ms. Rosen (for herself, Ms. Ernst , Mr. Risch , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo allow nonprofit child care providers to participate in certain loan programs of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Child Care Investment Act .\n#### 2. Small business loans for nonprofit child care providers\n##### (a) Business loan program\nSection 3(a) of the Small Business Act ( 15 U.S.C. 632(a) ) is amended by adding at the end the following:\n(10) Nonprofit child care providers (A) Definition In this paragraph, the term covered nonprofit child care provider means an organization\u2014 (i) that\u2014 (I) is in compliance with licensing requirements for child care providers of the State in which the organization is located; (II) is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code; (III) is primarily engaged in providing child care for children from birth to compulsory school age; and (IV) is in compliance with the size standards established under this subsection for business concerns in the applicable industry; (ii) for which each employee and regular volunteer complies with the criminal background check requirements under section 658H(b) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858f(b) ); (iii) that may\u2014 (I) provide care for school-age children outside of school hours or outside of the school year; or (II) offer preschool or prekindergarten educational programs; and (iv) subject to any exemption under Federal law applicable to the organization, that certifies to the Administrator that the organization will not discriminate in any business practice, including providing services to the public, on the basis of race, color, religion, sex, sexual orientation, marital status, age, disability, or national origin. (B) Eligibility for certain loan programs (i) In general Notwithstanding any other provision of this subsection, a covered nonprofit child care provider shall be deemed to be a small business concern for purposes of loans and financings under section 7(a). (ii) Prohibition on direct lending A loan or financing to a covered nonprofit child care provider made under the authority under clause (i) shall be made in cooperation with banks, certified development companies, or other financial institutions through agreements to participate on a deferred (guaranteed) basis. The Administrator is prohibited from making a direct loan or financing or entering an agreement to participate on an immediate basis for a loan or financing made to a covered nonprofit child care provider under the authority under clause (i). (iii) Loan guarantee A covered nonprofit child care provider\u2014 (I) shall obtain a guarantee of timely payment of the loan or financing from another person or entity to be eligible for such loan or financing of more than $500,000 under the authority under clause (i); and (II) may not be required to obtain a guarantee of timely payment of the loan or financing to be eligible for such loan or financing that is not more than $500,000 under the authority under clause (i). (C) Limitations (i) Basis for ineligibility The Administrator may not determine that a covered nonprofit child care provider is not eligible for a loan or financing described in subparagraph (B)(i) on the basis that the covered nonprofit child care provider is associated with an entity whose activities are protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. (ii) Use of funds A covered nonprofit child care provider receiving a loan or financing described in subparagraph (B)(i) may not use the proceeds of the loan or financing for a religious activity protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. .\n##### (b) 504 program\nSection 502 of the Small Business Investment Act of 1958 ( 15 U.S.C. 696 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Administration and inserting the following:\n(a) In general The Administration ; and\n**(2)**\nby adding at the end the following:\n(b) Nonprofit child care providers (1) Definition In this subsection, the term covered nonprofit child care provider has the meaning given that term in section 3(a)(10) of the Small Business Act ( 15 U.S.C. 636(a)(10) ). (2) Eligibility for certain loan programs (A) In general Notwithstanding any other provision of this title, a covered nonprofit child care provider shall be deemed to be a small business concern for purposes of loans and financings under this title. (B) Prohibition on direct lending A loan or financing to a covered nonprofit child care provider made under the authority under subparagraph (A) shall be made in cooperation with banks, certified development companies, or other financial institutions through agreements to participate on a deferred (guaranteed) basis. The Administrator is prohibited from making a direct loan or financing or entering an agreement to participate on an immediate basis for a loan or financing made to a covered nonprofit child care provider under the authority under subparagraph (A). (C) Loan guarantee A covered nonprofit child care provider\u2014 (i) shall obtain a guarantee of timely payment of the loan or financing from another person or entity to be eligible for such loan or financing of more than $500,000 under the authority under subparagraph (A); and (ii) may not be required to obtain a guarantee of timely payment of the loan or financing to be eligible for such loan or financing that is not more than $500,000 under the authority under subparagraph (A). (3) Limitations (A) Basis for ineligibility The Administrator may not determine that a covered nonprofit child care provider is not eligible for a loan or financing described in paragraph (2)(A) on the basis that the covered nonprofit child care provider is associated with an entity whose activities are protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. (B) Use of funds A covered nonprofit child care provider receiving a loan or financing described in paragraph (2)(A) may not use the proceeds of the loan or financing for a religious activity protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. .\n##### (c) Reporting\n**(1) Definition**\nIn this subsection, the term covered nonprofit child care provider has the meaning given the term in paragraph (10) of section 3(a) of the Small Business Act ( 15 U.S.C. 632(a) ), as added by subsection (a).\n**(2) Requirement**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Administrator of the Small Business Administration shall submit to Congress a report that contains\u2014\n**(A)**\nfor the year covered by the report\u2014\n**(i)**\nthe number of loans and financings made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) to covered nonprofit child care providers;\n**(ii)**\nthe amount of the loans and financings described in clause (i);\n**(iii)**\nthe number of loans and financings provided under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ) to covered nonprofit child care providers; and\n**(iv)**\nthe amount of the loans and financings described in clause (iii); and\n**(B)**\nany other information determined relevant by the Administrator.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s273rs.xml",
      "text": "II\nCalendar No. 9\n119th CONGRESS\n1st Session\nS. 273\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Ms. Rosen (for herself, Ms. Ernst , Mr. Risch , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nFebruary 10, 2025 Reported by Ms. Ernst , with an amendment Omit the part struck through and insert the part printed in italic\nA BILL\nTo allow nonprofit child care providers to participate in certain loan programs of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Child Care Investment Act .\n#### 2. Small business loans for nonprofit child care providers\n##### (a) Business loan program\nSection 3(a) of the Small Business Act ( 15 U.S.C. 632(a) ) is amended by adding at the end the following:\n(10) Nonprofit child care providers (A) Definition In this paragraph, the term covered nonprofit child care provider means an organization\u2014 (i) that\u2014 (I) is in compliance with licensing requirements for child care providers of the State in which the organization is located; (II) is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code; (III) is primarily engaged in providing child care for children from birth to compulsory school age; and (IV) is in compliance with the size standards established under this subsection for business concerns in the applicable industry; (ii) for which each employee and regular volunteer complies with the criminal background check requirements under section 658H(b) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858f(b) ); (iii) that may\u2014 (I) provide care for school-age children outside of school hours or outside of the school year; or (II) offer preschool or prekindergarten educational programs; and (iv) subject to any exemption under Federal law applicable to the organization, that certifies to the Administrator that the organization will not discriminate in any business practice, including providing services to the public, on the basis of race, color, religion, sex, sexual orientation, marital status, age, disability, or national origin. (B) Eligibility for certain loan programs (i) In general Notwithstanding any other provision of this subsection, a covered nonprofit child care provider shall be deemed to be a small business concern for purposes of loans and financings under section 7(a). (ii) Prohibition on direct lending A loan or financing to a covered nonprofit child care provider made under the authority under clause (i) shall be made in cooperation with banks, certified development companies, or other financial institutions through agreements to participate on a deferred (guaranteed) basis. The Administrator is prohibited from making a direct loan or financing or entering an agreement to participate on an immediate basis for a loan or financing made to a covered nonprofit child care provider under the authority under clause (i). (iii) Loan guarantee A covered nonprofit child care provider\u2014 (I) shall obtain a guarantee of timely payment of the loan or financing from another person or entity to be eligible for such loan or financing of more than $500,000 under the authority under clause (i); and (II) may not be required to obtain a guarantee of timely payment of the loan or financing to be eligible for such loan or financing that is not more than $500,000 under the authority under clause (i). (C) Limitations (i) Basis for ineligibility The Administrator may not determine that a covered nonprofit child care provider is not eligible for a loan or financing described in subparagraph (B)(i) on the basis that the covered nonprofit child care provider is associated with an entity whose activities are protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. (ii) Use of funds A covered nonprofit child care provider receiving a loan or financing described in subparagraph (B)(i) may not use the proceeds of the loan or financing for a religious activity protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. .\n##### (b) 504 program\nSection 502 of the Small Business Investment Act of 1958 ( 15 U.S.C. 696 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Administration and inserting the following:\n(a) In general The Administration ; and\n**(2)**\nby adding at the end the following:\n(b) Nonprofit child care providers (1) Definition In this subsection, the term covered nonprofit child care provider has the meaning given that term in section 3(a)(10) of the Small Business Act (15 U.S.C. 636(a)(10) 632(a)(10) ). (2) Eligibility for certain loan programs (A) In general Notwithstanding any other provision of this title, a covered nonprofit child care provider shall be deemed to be a small business concern for purposes of loans and financings under this title. (B) Prohibition on direct lending A loan or financing to a covered nonprofit child care provider made under the authority under subparagraph (A) shall be made in cooperation with banks, certified development companies, or other financial institutions through agreements to participate on a deferred (guaranteed) basis. The Administrator is prohibited from making a direct loan or financing or entering an agreement to participate on an immediate basis for a loan or financing made to a covered nonprofit child care provider under the authority under subparagraph (A). (C) Loan guarantee A covered nonprofit child care provider\u2014 (i) shall obtain a guarantee of timely payment of the loan or financing from another person or entity to be eligible for such loan or financing of more than $500,000 under the authority under subparagraph (A); and (ii) may not be required to obtain a guarantee of timely payment of the loan or financing to be eligible for such loan or financing that is not more than $500,000 under the authority under subparagraph (A). (3) Limitations (A) Basis for ineligibility The Administrator may not determine that a covered nonprofit child care provider is not eligible for a loan or financing described in paragraph (2)(A) on the basis that the covered nonprofit child care provider is associated with an entity whose activities are protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. (B) Use of funds A covered nonprofit child care provider receiving a loan or financing described in paragraph (2)(A) may not use the proceeds of the loan or financing for a religious activity protected under the First Amendment to the Constitution of the United States, as interpreted by the courts of the United States. .\n##### (c) Reporting\n**(1) Definition**\nIn this subsection, the term covered nonprofit child care provider has the meaning given the term in paragraph (10) of section 3(a) of the Small Business Act ( 15 U.S.C. 632(a) ), as added by subsection (a).\n**(2) Requirement**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Administrator of the Small Business Administration shall submit to Congress a report that contains\u2014\n**(A)**\nfor the year covered by the report\u2014\n**(i)**\nthe number of loans and financings made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) to covered nonprofit child care providers;\n**(ii)**\nthe amount of the loans and financings described in clause (i);\n**(iii)**\nthe number of loans and financings provided under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ) to covered nonprofit child care providers; and\n**(iv)**\nthe amount of the loans and financings described in clause (iii); and\n**(B)**\nany other information determined relevant by the Administrator.",
      "versionDate": "2025-02-10",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-01-15",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "7109",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Business Child Care Investment Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child care and development",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Preschool education",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-02-13T19:30:07Z"
          },
          {
            "name": "Tax-exempt organizations",
            "updateDate": "2025-02-13T19:30:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-04T12:06:38Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s273is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s273rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Small Business Child Care Investment Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "title": "Small Business Child Care Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Child Care Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T14:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow nonprofit child care providers to participate in certain loan programs of the Small Business Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T14:18:24Z"
    }
  ]
}
```
