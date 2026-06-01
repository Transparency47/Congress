# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7534
- Title: Contract Our Veterans Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7534
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-20T08:08:33Z
- Update date including text: 2026-05-20T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7534",
    "number": "7534",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Contract Our Veterans Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:33Z",
    "updateDateIncludingText": "2026-05-20T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "GA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "KY"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7534ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7534\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Fine (for himself, Mr. Van Orden , Mr. Donalds , and Mr. Hunt ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to establish a goal for participation by small business concerns owned and controlled by veterans in procurement contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Contract Our Veterans Act of 2026 .\n#### 2. Agency contracting goals for small business concerns owned and controlled by veterans\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended by inserting after section 36A the following new section:\n36B. Small business concerns owned and controlled by veterans (a) Contracting Officer Defined In this section, the term contracting officer has the meaning given such term in section 2101 of title 41, United States Code. (b) Sole source contracts for contracts above simplified acquisition threshold A contracting officer may award a contract to a small business concern owned and controlled by veterans using procedures other than competitive procedures if\u2014 (1) such concern is determined to be a responsible source with respect to performance of such contract; (2) the anticipated award price of the contract (including options) will not exceed the amounts specified in section 36(c)(2) of the Small Business Act ( 15 U.S.C. 657f(c)(2) ); and (3) the contracting officer determines the contract award can be made at a fair and reasonable price that offers best value to the United States. (c) Restricted competition A contracting officer shall award contracts on the basis of competition restricted to small business concerns owned and controlled by veterans if the contracting officer has a reasonable expectation that two or more small business concerns owned and controlled by veterans will submit offers and that the award can be made at a fair and reasonable price that offers best value to the United States. (d) Eligibility of small business concerns A small business concern may be awarded a contract under this section only if the small business concern and the veteran owner of the small business concern are listed in the database described in section 36(f)(1) of the Small Business Act ( 15 U.S.C. 657f(f)(1) ). .\n#### 3. Governmentwide goals and reporting requirements for small business concerns owned and controlled by veterans\n##### (a) Governmentwide goals\nSection 15(g) of the Small Business Act ( 15 U.S.C. 644(g) ) is amended\u2014\n**(1)**\nby striking and small business concerns owned and controlled by women and inserting , small business concerns owned and controlled by women, and small business concerns owned and controlled by veterans each place it appears;\n**(2)**\nin paragraph (1)(A), by adding at the end the following new clause:\n(vi) The Governmentwide goal for participation by small business concerns owned and controlled by veterans shall be established at not less than 5 percent of the total value of all prime contract and subcontract awards for each fiscal year. ; and\n**(3)**\nin paragraph (2)(A), by striking and by small business concerns owned and controlled by women and inserting by small business concerns owned and controlled by women, and by small business concerns owned and controlled by veterans, .\n##### (b) Reporting on goals\nSection 15(h)(2) of the Small Business Act ( 15 U.S.C. 644(h)(2) ) is amended\u2014\n**(1)**\nin subparagraph (E)\u2014\n**(A)**\nin clauses (i)(VI), (ii)(VII), (iii)(VIII), and (iv)(VIII), by inserting small business concerns owned and controlled by veterans after small business concerns owned and controlled by women, ;\n**(B)**\nin clause (vii)(VI), by striking and at the end;\n**(C)**\nin clause (viii)(X), by inserting small business concerns owned and controlled by veterans after small business concerns owned and controlled by socially and economically disadvantaged individuals, ; and\n**(D)**\nby adding at the end the following new clause:\n(ix) small business concerns owned and controlled by veterans\u2014 (I) in the aggregate; (II) through sole source contracts; (III) through competitions restricted to small business concerns; (IV) through competitions restricted to small business concerns owned and controlled by veterans; (V) through unrestricted competition; (VI) that were purchased by another entity after the initial contract was awarded and as a result of the purchase, would no longer be deemed to be small business concerns owned and controlled by veterans for purposes of the initial contract; and (VII) that were awarded using a procurement method that restricted competition to small business concerns owned and controlled by service-disabled veterans, qualified HUBZone small business concerns, small business concerns owned and controlled by socially and economically disadvantaged individuals, small business concerns owned and controlled by women, or a subset of any such concerns; and ; and\n**(2)**\nin subparagraph (F), by striking and small business concerns owned and controlled by women and inserting , small business concerns owned and controlled by women, and small business concerns owned and controlled by veterans .\n#### 4. Participation in Federal procurement by small business concerns owned and controlled by veterans\n##### (a) Business Opportunity Specialists\nSection 4(g)(1) of the Small Business Act ( 15 U.S.C. 633(g)(1) )\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking and 36 and inserting 36, and 36B ;\n**(2)**\nin subparagraph (A)(v), by striking 36, and and inserting 36, 36B, and ; and\n**(3)**\nin subparagraph (D), by striking 36, or and inserting 36, 36B, or .\n##### (b) Commercial market representative\nSection 4(h)(1) of the Small Business Act ( 15 U.S.C. 633(g)(1) ) in the matter preceding subparagraph (A), by striking and 36 and inserting 36, and 36B .\n##### (c) Consideration of offers\nSection 8(a)(17)(A) of the Small Business Act ( 15 U.S.C. 637(a)(17)(A) ) is amended by striking or section 36 and inserting section 36, or section 36B .\n##### (d) Best in class addendum\nSection 15(h)(4)(A)(ii) of the Small Business Act ( 15 U.S.C. 644(h)(4)(A)(ii) ) is amended\u2014\n**(1)**\nin subclause (III), by striking and at the end;\n**(2)**\nin subclause (IV), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subclause:\n(V) small business concerns owned and controlled by veterans. .\n##### (e) Offices of Small and Disadvantaged Business Utilization\nSection 15(k) of the Small Business Act ( 15 U.S.C. 644(k) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking or 44 and inserting 36B, or 44 ;\n**(2)**\nby striking and 44 and inserting 36B, and 44 each place it appears; and\n**(3)**\nby striking or 36 and inserting 36, or 36B each place it appears.\n##### (f) Scorecard Program\nSection 15(y) of the Small Business Act ( 15 U.S.C. 644(y) ) is amended\u2014\n**(1)**\nby striking and small business concerns owned and controlled by women and inserting , small business concerns owned and controlled by women, and small business concerns owned and controlled by veterans each place it appears; and\n**(2)**\nin paragraph (4), by adding at the end the following new subparagraph:\n(E) The number (expressed as a percentage) and total dollar amount of awards made to small business concerns owned and controlled by veterans through sole source contracts and competitions restricted to small business concerns owned and controlled by veterans under section 36B. .\n##### (g) Mentor-Protege reporting\nSection 45(c)(1)(B) of the Small Business Act ( 15 U.S.C. 657r(c)(1)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (iii) through (v) as clauses (iv) through (vi), respectively; and\n**(2)**\nby inserting after clause (ii) the following new clause:\n(iii) small business concerns owned and controlled by veterans; .\n##### (h) Limitations on subcontracting\nSection 46 of the Small Business Act ( 15 U.S.C. 657s ) is amended\u2014\n**(1)**\nin subsection (a), by striking or 36 and inserting 36, or 36B ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (D), by striking or at the end;\n**(ii)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) with respect to a contract awarded under section 36B, is a small business concern owned and controlled by veterans. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (E), by striking or at the end;\n**(ii)**\nin subparagraph (F), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(G) if a subcontractor for a small business concern owned and controlled by veterans, is such a concern. .",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-03-03",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "3964",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Contract Our Veterans Act of 2026",
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
        "updateDate": "2026-03-16T12:19:55Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7534ih.xml"
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
      "title": "Contract Our Veterans Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-14T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Contract Our Veterans Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to establish a goal for participation by small business concerns owned and controlled by veterans in procurement contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:31Z"
    }
  ]
}
```
