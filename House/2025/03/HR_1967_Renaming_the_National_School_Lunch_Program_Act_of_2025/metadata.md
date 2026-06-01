# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1967?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1967
- Title: Renaming the National School Lunch Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1967
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1967",
    "number": "1967",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Renaming the National School Lunch Program Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IN"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "TN"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "DC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "VA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1967ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1967\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mrs. Watson Coleman (for herself, Mr. Green of Texas , Mr. Carson , Mr. Cohen , Ms. Barrag\u00e1n , Mr. Meeks , Mr. Evans of Pennsylvania , Ms. Norton , Ms. Clarke of New York , Ms. McClellan , Mrs. McIver , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo rename the Richard B. Russell National School Lunch Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Renaming the National School Lunch Program Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThat Jean E. Fairfax was a civil rights activist who\u2014\n**(A)**\nwas born to parents who were the first in their family to be legally free;\n**(B)**\nfought for equitable educational access, challenged systemic employment discrimination, and led influential federal policy innovations in all realms to support working class and marginalized peoples;\n**(C)**\nassisted Black families navigating school integration after the ruling of Brown v. Board of Education;\n**(D)**\njoined the National Association for the Advancement of Colored People\u2019s Legal Defense Fund and established the Division of Legal Information and Community Service; and\n**(E)**\ncontinued to serve her community through civil rights work and philanthropy after retirement.\n**(2)**\nIt is evidenced that Jean E. Fairfax contributed greatly to the National School Lunch Program in an equitable manner through\u2014\n**(A)**\norganizing five national women\u2019s organizations and creating the Committee on School Lunch Participation to study the National School Lunch Program;\n**(B)**\ntestifying before Congress on multiple occasions to reveal that the implementation of the National School Lunch Program was failing to reach children that needed it most;\n**(C)**\nadvocating for increased funding of the National School Lunch Program to serve children in areas of concentrated poverty that were disproportionately minorities; and\n**(D)**\nhaving her findings incorporated in National School Lunch Program reform legislation that led to the program becoming more inclusive.\n**(3)**\nThe National School Lunch Program is named after an individual who\u2014\n**(A)**\nobjected to anti-lynching bills and civil rights legislation in Congress and affirmed his belief in white supremacy;\n**(B)**\nopposed school integration and was a contributor to the creation of the Southern Manifesto;\n**(C)**\ndismissed concerns of child-welfare advocates, civil rights activists, and women-led organizations during debate over the implementation of the National School Lunch Program; and\n**(D)**\nbelieved that segregation should be maintained while implementing the National School Lunch Program.\n#### 3. Renaming of Richard B. Russell National School Lunch Act\n##### (a) Short title\nThe first section of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 note) is amended by striking Richard B. Russell National School Lunch Act and inserting Jean E. Fairfax National School Lunch Act .\n##### (b) Conforming amendments\nEach of the following provisions of law is amended by striking Richard B. Russell National School Lunch Act and inserting Jean E. Fairfax National School Lunch Act :\n**(1)**\nSections 3(a)(2)(C), 3(b)(1)(A)(iii)(III), 3(e)(1)(D)(iii)(III), 17(b)(2), and 18(3)(A) of the Commodity Distribution Reform Act and WIC Amendments of 1987 ( 7 U.S.C. 612c note).\n**(2)**\nSection 5(l)(2)(D) of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note).\n**(3)**\nSection 10603(b) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 612c\u20134(b) ).\n**(4)**\nSections 4301(b)(2), 4301(b)(3), 4304(a)(2)(A), 4304(a)(2)(B), 4305(c), 4305(c)(1), 4306(a)(3), 4306(b), 14222(b)(1), 14222(c), and 14222(e)(1) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 612c\u20136(b)(1) , 612c\u20136(c), 612c\u20136(e)(1) 2208 note; 42 U.S.C. 1755a , 1758(b)(2), 1758(b)(3), 1769a note).\n**(5)**\nSection 404 of the Agricultural Act of 1949 ( 7 U.S.C. 1424 ).\n**(6)**\nSection 282(f)(2)(b) of the Act entitled To provide for further research into basic laws and principles relating to agriculture and to improve and facilitate the marketing and distribution of agricultural products , approved August 14, 1946 (7 U.S.C 1638a(f)(2)(b)).\n**(7)**\nSection 201(a) of the Act entitled An Act to extend the Agricultural Trade Development and Assistance Act of 1954, and for other purposes , approved September 21, 1959 ( 7 U.S.C. 1431c(a) ).\n**(8)**\nSections 1101(e), 2102(a), 2102(b), 2102(c), 2102(d)(1), 2202(a)(1), 2202(a)(2)(A), 2202(b), 2202(c), 2202(e)(2)(A)(ii), 2202(f)(1)(A), 2202(f)(1)(C), 2201(f)(1)(D), and 2202(f)(3), of the Families First Coronavirus Response Act ( 7 U.S.C. 2011 note; 42 U.S.C. 1760 note).\n**(9)**\nSections 11(u)(1), 11(u)(2)(A), and 11(u)(2)(B), of the Food Stamp Act of 1977 ( 7 U.S.C. 2020(u)(1) , 2020(u)(2)(A), 2020(u)(2)(B)).\n**(10)**\nSection 28(a)(1)(B) of the Food Stamp Act of 1964 ( 7 U.S.C. 2036a(a)(1)(B) ).\n**(11)**\nSection 211(a) of the Agricultural Trade Suspension Adjustment Act of 1980 (title II of the Agricultural Act of 1980) ( 7 U.S.C. 4004(a) ).\n**(12)**\nSections 413(b)(2) and 413(b)(3) of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7633(b)(2) , 7633(b)(3)).\n**(13)**\nSections 403(c)(2)(C), 422(b)(3), 423(d)(3), 741(a)(1), 742(a), and 742(b)(2)(A) and the caption for section 742 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1183a note, 1613(c)(2)(C), 1615(a), 1615(b)(2)(A), 1632(b)(3); 42 U.S.C. 1751 note).\n**(14)**\nSection 245A(h)(4)(A) of the Immigration and Nationality Act approved June 27, 1952, ( 8 U.S.C. 1255a(h)(4)(A) ).\n**(15)**\nSection 645(a)(3)(C)(iii) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( 10 U.S.C. 1060a note).\n**(16)**\nSections 1154(a)(2)(A)(i), 1154(a)(3)(A), and 2243(b) of title 10, United States Code.\n**(17)**\nSections 200(11)(A)(i)(II), 200(11)(A)(ii)(I), 200(11)(A)(ii)(II), 200(11)(B)(ii)(I)(bb), 404B(1)(A), 479, 483(a)(2)(ii)(XVII)(cc), 894(b)(1)(B), and 894(b)(5) of the Higher Education Act of 1965 ( 20 U.S.C. 1021(11)(A)(i)(II) , 1021(11)(A)(ii)(I), 1021(11)(A)(ii)(II), 1021(11)(B)(ii)(I)(bb), 1070a\u201322(d)(1)(A), 1087ss(d)(2)(C), 1090 note, 1161y(b)(1)(B), 1161y(b)(5)).\n**(18)**\nSection 444 of the Elementary and Secondary Education Amendments of 1967 ( 20 U.S.C. 1232g(b)(1)(K) ).\n**(19)**\nSections 1113(a)(5)(A), 2221(b)(3)(B)(i), 4611(d)(2)(B), and 7003(b)(2)(B)(i)(III)(bb)(BB) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5)(A) , 6641(b)(3)(B)(i), 7261(d)(2)(B), 7703(b)(2)(B)(i)(III)(bb)(BB)).\n**(20)**\nSection 6122(3) of the America COMPETES Act ( 20 U.S.C. 9832(3) ).\n**(21)**\nSection 423(j)(2)(D) of the Federal Food, Drug, and Cosmetic Act (21 U.S.C 350l(j)(2)(D)).\n**(22)**\nSection 3(36)(A)(iv) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(36)(A)(iv) ).\n**(23)**\nSection 3803(c)(2)(C)(xiii) of title 31, United States Code.\n**(24)**\nSection 252(i) of the Juvenile Justice and Delinquency Prevention Act 1974 ( 34 U.S.C. 11162(i) ).\n**(25)**\nSection 402a(f)(2)(A) of title 37, United States Code.\n**(26)**\nSection 113(e)(8)(A) of title 40, United States Code.\n**(27)**\nSections 722(b)(3)(A)(i), 722(b)(3)(B)(i), 722(b)(3)(C)(i), 722(b)(3)(D)(i), 722(d)(3), 722(d)(4)(A), 722(d)(5), 722(d)(7), 722(d)(11)(A), and 722(d)(13) of title VII of division N and section 904(a)(6)(B) of title IX of division N of the Consolidated Appropriations Act, 2021 ( 42 U.S.C. 1751 note; 47 U.S.C. 1752(a)(6)(B) ).\n**(28)**\nSections 222(3), 307(b)(1), 307(b)(1)(A), 307(b)(2), and 336(a) of the Healthy, Hunger-Free Kids Act of 2010 ( 42 U.S.C. 1751 note, 1766 note).\n**(29)**\nSections 2(4), 125, 301(a), 301(b)(1), 301(a), 301(b)(1), 301(b)(2), and 301(b)(3) of the Healthy Meals for Healthy Americans Act of 1994 ( 42 U.S.C. 1751 note).\n**(30)**\nSections 2(a)(1), 2(d)(1), 2(d)(2), 3(a)(1), and 3(b) of the Keep Kids Fed Act of 2022 ( 42 U.S.C. 1753 note, 1760 note, 1766 note).\n**(31)**\nSections 4033(b)(3)(B), 4213(c), 4213(c)(1), and 4214(a) of the Agricultural Act of 2014 ( 25 U.S.C. 1685(b)(3)(B) ; 42 U.S.C. 1755b(c) ; 1755b(c)(1), 1769a note).\n**(32)**\nSection 4207(a)(1) of the Agriculture Improvement Act of 2018 ( 42 U.S.C. 1760 note).\n**(33)**\nSections 1107(a), 1107(b), and 1107(c)(1) of the American Rescue Plan Act of 2021 ( 42 U.S.C. 1766 note).\n**(34)**\nSections 119(i), 119(j)(1), and 119(j)(3)(C) of the Child Nutrition and WIC Reauthorization Act of 2004 ( 42 U.S.C. 1766 note).\n**(35)**\nSections 3(a)(1), 3(a)(2), 3(a)(5), 3(b), 4(b)(1)(B), 4(b)(2)(B)(ii), 4(b)(3), 4(b)(4), 4(e)(1)(A), 7(a)(1)(A), 7(a)(2)(A), 7(a)(3), 7(a)(4), 7(a)(6), 7(a)(7), 7(a)(8), 7(a)(9)(A), 7(e)(3), 7(f), 7(g)(1)(A)(ii)(I), 7(g)(1)(B), 7(g)(1)(D)(i), 7(g)(1)(D)(ii), 7(h)(2)(A), 7(i)(3)(A), 7(i)(3)(B)(ii), 10(a), 10(b)(1)(a), 10(c), 11, 13, 16(b), 19(d), 19(h)(3)(D), 19(h)(5)(B)(vi), and 23(d)(2) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1772(a)(1) , 1772(a)(2), 1772(a)(5), 1772(b), 1773(b)(1)(B), 1773(b)(2)(B)(ii), 1773(b)(3), 1773(b)(4), 1773(e)(1)(A), 1776(a)(1)(A), 1776(a)(2)(A), 1776(a)(3), 1776(a)(4), 1776(a)(6), 1776(a)(7), 1776(a)(8), 1776(a)(9)(A), 1776(e)(3), 1776(f), 1776(g)(1)(A)(ii)(I), 1776(g)(1)(B), 1776(g)(1)(D)(i), 1776(g)(1)(D)(ii), 1776(h)(2)(A), 1776(i)(3)(A), 1776(i)(3)(B)(ii), 1779(a), 1779(b)(1)(a), 1779(c), 1780(c), 1782, 1785(b), 1788(d), 1788(h)(3)(D), 1788(h)(5)(B)(vi), 1793(d)(2)).\n**(36)**\nSection 4(8)(A) of the National Science Foundation Authorization Act of 2002 ( 42 U.S.C. 1862n note).\n**(37)**\nSection 3(c)(6)(B) of the STEM Education Act of 2015 ( 42 U.S.C. 1862q(c)(6)(B) ).\n**(38)**\nSections 658E(c)(2)(E)(i)(IV) and 658O(b)(3) of the Omnibus Budget Reconciliation Act of 1981 ( 42 U.S.C. 9858m(b)(3) , 9858c(c)(2)(E)(i)(IV)).\n**(39)**\nSection 40541(d)(1)(B)(i) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18831(d)(1)(B)(i) ).\n**(40)**\nSubsection (b) of the first section of the Act entitled An Act to extend the application of certain laws to American Samoa , as approved September 25, 1962 ( 48 U.S.C. 1666(b) ).",
      "versionDate": "2025-03-06",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-05T15:49:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1967",
          "measure-number": "1967",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1967v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Renaming the National School Lunch Program Act of 2025</strong></p><p>This bill renames the Richard B. Russell National School Lunch Act as the Jean E. Fairfax National School Lunch Act.</p>"
        },
        "title": "Renaming the National School Lunch Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1967.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Renaming the National School Lunch Program Act of 2025</strong></p><p>This bill renames the Richard B. Russell National School Lunch Act as the Jean E. Fairfax National School Lunch Act.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr1967"
    },
    "title": "Renaming the National School Lunch Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Renaming the National School Lunch Program Act of 2025</strong></p><p>This bill renames the Richard B. Russell National School Lunch Act as the Jean E. Fairfax National School Lunch Act.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr1967"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1967ih.xml"
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
      "title": "Renaming the National School Lunch Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Renaming the National School Lunch Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To rename the Richard B. Russell National School Lunch Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:26Z"
    }
  ]
}
```
