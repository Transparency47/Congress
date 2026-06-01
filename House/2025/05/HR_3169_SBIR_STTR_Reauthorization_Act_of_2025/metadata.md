# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3169?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3169
- Title: SBIR/STTR Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3169
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-02-18T13:56:14Z
- Update date including text: 2026-02-18T13:56:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3169",
    "number": "3169",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SBIR/STTR Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-18T13:56:14Z",
    "updateDateIncludingText": "2026-02-18T13:56:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:07:35Z",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "RI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NH"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3169ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3169\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Ms. Vel\u00e1zquez introduced the following bill; which was referred to the Committee on Small Business , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Small Business Act to reauthorize and modify the Small Business Innovation Research and Small Business Technology Transfer Research programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SBIR/STTR Reauthorization Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTitle I\u2014Reauthorization of Programs\nSec. 101. Extension of SBIR and STTR authority.\nSec. 102. Extension of FAST Program.\nTitle II\u2014Enhancing Competition\nSec. 201. Increasing agency expenditures for SBIR and STTR programs.\nSec. 202. SBIR and STTR fellowships.\nSec. 203. Application assistance to broaden participation.\nSec. 204. Technical and business assistance improvements.\nSec. 205. Improvements to website relating to the SBIR program or STTR program.\nTitle III\u2014Commercialization Improvements\nSec. 301. Phase III award education.\nSec. 302. Technology Commercialization Official.\nSec. 303. Phase III improvements.\nTitle IV\u2014Pilot Programs\nSec. 401. Extend and modify assistance for administrative, oversight, and contract processing costs.\nSec. 402. Extend and expand the direct to Phase II authority.\nSec. 403. Extend commercialization readiness program for civilian agencies.\nSec. 404. Extension of certain SBIR and STTR pilot programs.\nSec. 405. Extension of due diligence program to assess security risks.\nTitle V\u2014Oversight and Simplification Initiatives\nSec. 501. Annual reports to Congress.\nSec. 502. Comptroller General report on diversification and commercialization.\nSec. 503. Extend the report on award timeliness.\nSec. 504. Pilot program to accelerate National Institutes of Health evaluation process.\nSec. 505. Codifying safeguards for small business concerns majority-owned by venture capital operating companies, hedge funds, or private equity firms.\nSec. 506. Commercialization impact assessment.\nTitle VI\u2014Technical Changes\nSec. 601. Inclusion of SBICs in the SBIR and STTR programs.\nSec. 602. Phase III and sole-source awards.\nI\nReauthorization of Programs\n#### 101. Extension of SBIR and STTR authority\n##### (a) SBIR\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended by striking subsection (m).\n##### (b) STTR\nSection 9(n)(1)(A) of the Small Business Act ( 15 U.S.C. 638(n)(1)(A) ) is amended by striking through fiscal year 2025 .\n#### 102. Extension of FAST Program\nSection 34(i) of the Small Business Act ( 15 U.S.C. 657d(i) ) is amended by striking September 30, 2005 and inserting September 30, 2030 .\nII\nEnhancing Competition\n#### 201. Increasing agency expenditures for SBIR and STTR programs\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin subsection (f)(1)\u2014\n**(A)**\nin subparagraph (H), by striking and ;\n**(B)**\nin subparagraph (I), by striking fiscal year 2017 and each fiscal year thereafter, and inserting each of fiscal years 2017 through 2025; ; and\n**(C)**\nby inserting after subparagraph (I) the following new subparagraphs:\n(J) not less than 4 percent of such budget in fiscal years 2026 and 2027; (K) not less than 5 percent of such budget in fiscal years 2028 and 2029; (L) not less than 6 percent of such budget in fiscal years 2030 and 2031; and (M) not less than 7 percent of such budget in fiscal year 2032 and each fiscal year thereafter, ; and\n**(2)**\nin subsection (n)(1)(B)\u2014\n**(A)**\nin clause (iv), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (v), by striking fiscal year 2016 and each fiscal year thereafter. and inserting each of fiscal years 2016 through 2025; ; and\n**(C)**\nby adding at the end the following:\n(vi) 0.5 percent for fiscal year 2026 and 2027; (vii) 0.65 percent for fiscal year 2028 and 2029; (viii) 0.8 percent for fiscal year 2030 and 2031; and (ix) 1 percent for fiscal year 2032 and each fiscal year thereafter. .\n#### 202. SBIR and STTR fellowships\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin subsection (f), by adding at the end the following new paragraph:\n(5) Fellowships (A) In general A Federal agency may provide grants or awards, either directly or in partnership with a third party, to small business concerns that have received SBIR or STTR Phase II awards to provide fellowship and internship opportunities at the undergraduate, baccalaureate, graduate, and postdoctoral levels in fields that are important to such Federal agency. (B) Enhanced outreach Each Federal agency that makes an award or enters into a partnership under subparagraph (A) shall provide for enhanced outreach to increase the participation of women, socially disadvantaged individuals (as described in section 8(a)(5)), and economically disadvantaged individuals (as described section 8(a)(6)(A)) in the fellowship and internship opportunities described under subparagraph (A). (C) Support organization Each Federal agency that makes an award or enters into a partnership under subparagraph (A) may partner with or provide grants or awards to a third-party organization to support and facilitate the enhanced outreach under subparagraph (B) provided that such third-party organization is a nonprofit organization with relevant experience and demonstrated expertise in delivery of services described in subparagraph (B). (D) Funding In carrying out this paragraph, a Federal agency may use only the following amounts: (i) With respect to a Federal agency that uses the authority under subsection (mm), the funds authorized under such subsection. (ii) With respect a Federal agency other than a Federal agency described in clause (i), not more than three percent of the funds required to be expended under paragraph (1). ; and\n**(2)**\nin subsection (n), by adding at the end the following new paragraph:\n(4) Fellowships (A) In general A Federal agency may provide grants or awards, either directly or in partnership with a third party, to small business concerns that have received SBIR or STTR Phase II awards to provide fellowship and internship opportunities at the undergraduate, baccalaureate, graduate, and postdoctoral levels in fields that are important to such Federal agency. (B) Enhanced outreach Each Federal agency that makes an award or enters into a partnership under subparagraph (A) shall provide for enhanced outreach to increase the participation of women, socially disadvantaged individuals (as described in section 8(a)(5)), and economically disadvantaged individuals (as described section 8(a)(6)(A)) in the fellowship and internship opportunities described under subparagraph (A). (C) Support organization Each Federal agency that makes an award or enters into a partnership under subparagraph (A) may partner with or provide grants or awards to a third-party organization to support and facilitate the enhanced outreach under subparagraph (B) provided such third-party organization is a nonprofit organization with relevant experience and demonstrated expertise in delivery of services described in subparagraph (B). (D) Funding In carrying out this paragraph, a Federal agency may use only the following amounts: (i) With respect to a Federal agency that uses the authority under subsection (mm), the funds authorized under such subsection. (ii) With respect a Federal agency other than a Federal agency described in clause (i), not more than three percent of the funds required to be expended under paragraph (1). .\n#### 203. Application assistance to broaden participation\n##### (a) In general\nSection 9(mm)(1) of the Small Business Act ( 15 U.S.C. 638(mm)(1) ) is amended\u2014\n**(1)**\nin subparagraph (J), by striking and at the end;\n**(2)**\nin subparagraph (K), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(L) providing small business concerns with assistance applying to the SBIR program or STTR program of the Federal agency, including providing such assistance to carry out the policy directive required under paragraphs (2)(F) or (5) of subsection (j) and subsection (p)(2)(H) to increase the participation of States with respect to which a low level of SBIR or STTR awards have historically been awarded. .\n##### (b) Enhanced minority institution participation\n**(1) SBIR**\nSection 9(j) of the Small Business Act ( 15 U.S.C. 638(j) ), is amended by adding at the end the following new paragraph:\n(5) Increased outreach requirements Not later than 90 days after the date of the enactment of this paragraph, the Administration shall modify the policy directives issued pursuant to this subsection to require enhanced outreach efforts to increase the participation of individuals conducting research at minority institutions (as defined in section 365 of the Higher Education Act of 1965 ( 20 U.S.C. 1067k )) and Hispanic-serving institutions (as defined in section 502(a) of such Act ( 20 U.S.C. 1101a(a) )) in SBIR programs. .\n**(2) STTR**\nSection 9(p)(2) of the Small Business Act ( 15 U.S.C. 638(p)(2) ) is amended\u2014\n**(A)**\nin subparagraph (F), by striking and at the end;\n**(B)**\nin subparagraph (G)(iii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(H) procedures for outreach efforts to increase the participation of individuals conducting research at minority institutions (as defined in section 365 of the Higher Education Act of 1965 ( 20 U.S.C. 1067k )) and Hispanic-serving institutions (as defined in section 16 502(a) of such Act ( 20 U.S.C. 1101a(a) )) in STTR programs. .\n#### 204. Technical and business assistance improvements\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin subsection (q)\u2014\n**(A)**\nin paragraph (1), in the matter preceding subparagraph (A)\u2014\n**(i)**\nby striking may enter into an agreement with 1 or more vendors selected under paragraph (2)(A) to provide small business concerns engaged in SBIR or STTR projects with technical and business assistance services and inserting shall authorize recipients of awards under the SBIR program or the STTR program to select, if desired, technical and business assistance provided under subparagraph (A), (B), or (C) of paragraph (3) to provide such recipients with ;\n**(ii)**\nby inserting cybersecurity assistance, after intellectual property protections, ; and\n**(iii)**\nby striking such concerns and inserting such recipients ;\n**(B)**\nin paragraph (2), by adding at the end the following:\n(C) Staff A small business concern may, by contract or otherwise, use funding provided under this section to hire new staff, augment staff, or direct staff to conduct or participate in training activities consistent with the goals listed in paragraph (1) consistent with the goals listed in paragraph (1). ;\n**(C)**\nin paragraph (3), by striking subparagraphs (A) and (B) and inserting the following:\n(A) Phase I A Federal agency described in paragraph (1) shall authorize a recipient of a Phase I SBIR or STTR award to use not more than $6,500 per project, included as part of the award of the recipient or in addition to the amount of the award of the recipient as determined appropriate by the head of the Federal agency, for the services described in paragraph (1)\u2014 (i) provided through a vendor selected under paragraph (2)(A); (ii) provided through a vendor other than a vendor selected under paragraph (2)(A); (iii) achieved through the activities described in paragraph (2)(C); or (iv) provided through any combination of clauses (i) and (ii). (B) Phase II A Federal agency described in paragraph (1) shall authorize a recipient of a Phase II SBIR or STTR award to use not more than $50,000 per project, included as part of the award of the recipient or in addition to the amount of the award of the recipient as determined appropriate by the head of the Federal agency, for the services described in paragraph (1)\u2014 (i) provided through a vendor selected under paragraph (2)(A); (ii) provided through a vendor other than a vendor selected under paragraph (2)(A); (iii) achieved through the activities described in paragraph (2)(C); or (iv) provided through any combination of clauses (i), (ii), and (iii). ; and\n**(D)**\nby adding at the end the following:\n(5) Targeted review A Federal agency may perform targeted reviews of technical and business assistance funding as described in subsection (mm)(1)(F). ; and\n**(2)**\nby adding at the end the following:\n(aaa) I-Corps Participation (1) In general Each Federal agency that, as of January 1, 2025, was required to conduct an SBIR or STTR program with an Innovation Corps program (established under section 601 of the American Innovation and Competitiveness Act ( 42 U.S.C. 1862s\u20138 ) and commonly known as I\u2013Corps ) shall\u2014 (A) provide an option for participation in an I\u2013Corps teams course, I\u2013Corps bootcamp, or another equivalent training program to recipients of an award under the SBIR or STTR program; and (B) authorize the recipients described in subparagraph (A) to use amounts authorized under this subsection to participate in the I\u2013Corps teams course, I\u2013Corps bootcamp, or another equivalent training program. (2) Cost of participation The cost of participation by a recipient described in paragraph (1)(A) in an I\u2013Corps course, I\u2013Corps bootcamp, or another equivalent training program may be provided by\u2014 (A) an I\u2013Corps team grant; (B) funds awarded to the recipient under this subsection; (C) the participating teams or other sources as appropriate; or (D) any combination of sources described in subparagraphs (A), (B), and (C). .\n#### 205. Improvements to website relating to the SBIR program or STTR program\n##### (a) SBIR program\nSection 9(g)(8) of the Small Business Act ( 15 U.S.C. 638(g)(8) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by adding and at the end; and\n**(3)**\nby adding at the end the following new subparagraph:\n(D) for each research institution subcontracted by a recipient of a Phase I, Phase II, or Phase III SBIR award to perform research or research and development with respect to such award\u2014 (i) the name and location of such research institution; (ii) whether such research institution is\u2014 (I) an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); (II) a nonprofit institution (as defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )) other than an institution of higher education; or (III) a federally funded research and development center (as identified by the National Scientific Foundation in accordance with the Federal Acquisition Regulation); and (iii) for each research institution that is an institution of higher education, whether such research institution is\u2014 (I) a part B institution (as defined in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )); (II) a Hispanic-serving institution (as defined in section 502 of such Act ( 20 U.S.C. 1101a )); (III) a Tribal College or University (as defined in section 316 of such Act ( 20 U.S.C. 1059c )); (IV) an Alaska Native-serving institution or a Native Hawaiian-serving institution (as defined in section 317(b) of such Act ( 20 U.S.C. 1059d(b) )); (V) a Predominantly Black Institution (as defined in section 371(c) of such Act ( 20 U.S.C. 1067q(c) )); (VI) an Asian American and Native American Pacific Islander-serving institution (as defined in section 371(c) of such Act (20 U.S.C. 10 1067q(c))); or (VII) a Native American-serving nontribal institution (as defined in section 371(c) of such Act ( 20 U.S.C. 1067q(c) )); .\n##### (b) STTR program\nSection 9(o)(9) of the Small Business Act ( 15 U.S.C. 638(o)(9) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by adding and at the end; and\n**(3)**\nby adding at the end the following new subparagraph:\n(D) for each research institution subcontracted by a recipient of a Phase I or Phase II STTR award to perform research or research and development with respect to such award\u2014 (i) the name and location of such research institution; (ii) whether such research institution is\u2014 (I) an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); (II) a nonprofit institution (as defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )) other than an institution of higher education; or (III) a federally funded research and development center (as identified by the National Scientific Foundation in accordance with the Federal Acquisition Regulation); and (iii) for each research institution that is an institution of higher education, whether such research institution is\u2014 (I) a part B institution (as defined in section 322 the Higher Education Act of 1965 ( 20 U.S.C. 1061 )); (II) a Hispanic-serving institution (as defined in section 502 of such Act ( 20 U.S.C. 1101a )); (III) a Tribal College or University (as defined in section 316 of such Act ( 20 U.S.C. 1059c )); (IV) an Alaska Native-serving institution or a Native Hawaiian-serving institution (as defined in section 317(b) of such Act ( 20 U.S.C. 1059d(b) )); (V) a Predominantly Black Institution (as defined in section 371(c) of such Act ( 20 U.S.C. 1067q(c) )); (VI) an Asian American and Native American Pacific Islander-serving institution (as defined in section 371(c) of such Act (20 U.S.C. 25 1067q(c))); or (VII) a Native American-serving nontribal institution (as defined in section 371(c) of such Act ( 20 U.S.C. 1067q(c) )); .\n##### (c) Database reporting\n**(1) In general**\nSection 9(k) of the Small Business Act ( 15 U.S.C. 638(k) ) is amended\u2014\n**(A)**\nby striking Phase I or Phase II SBIR or STTR each place it appears and inserting Phase I, Phase II, or Phase III SBIR or STTR ;\n**(B)**\nin paragraph (1)(B)\u2014\n**(i)**\nin clause (ii), by striking and at the end;\n**(ii)**\nin clause (iii), by adding and at the end; and\n**(iii)**\nby adding at the end the following new clause:\n(iv) information regarding any research institution subcontracted by such small business concern to perform research or research and development with respect to such award, including\u2014 (I) the name and location of such research institution; (II) whether such research institution is\u2014 (aa) an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); (bb) a nonprofit institution (as defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )) other than an institution of higher education; or (cc) a federally funded research and development center (as identified by the National Scientific Foundation in accordance with the Federal Acquisition Regulation); and (III) for each research institution that is an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )), whether such research institution is an institution described in paragraphs (1) through (7) of section 371(a) of such Act ( 20 U.S.C. 1067q(a) ); ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking Phase I or Phase II of the SBIR program or the STTR and inserting Phase I, Phase II, or Phase III of the SBIR program or the STTR ;\n**(ii)**\nin subparagraph (F), by striking and at the end;\n**(iii)**\nin subparagraph (G)(ii), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following new subparagraph:\n(H) contains information for each research institution subcontracted by a recipient of a Phase I, Phase II, or Phase III STTR or SBIR award to perform research or research and development with respect to such award, including\u2014 (i) the name and location of such research institution; (ii) whether such research institution is\u2014 (I) an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); (II) a nonprofit institution (as defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )) other than an institution of higher education; or (III) a federally funded research and development center (as identified by the National Scientific Foundation in accordance with the Federal Acquisition Regulation); and (iii) for each research institution that is an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )), whether such research institution is an institution described in paragraphs (1) through (7) of section 371(a) of such Act ( 20 U.S.C. 1067q(a) ). ; and\n**(D)**\nin paragraph (3)(C), by striking Phase I or Phase II award each place it appears and inserting Phase I, Phase II, or Phase III award .\n**(2) Database update deadline**\nNotwithstanding paragraphs (1) or (2) of section 9(k) of the Small Business Act ( 15 U.S.C. 638(k) ), the Administrator shall, not later than 1 year after the date of the enactment of this Act, include\u2014\n**(A)**\nin the database described such paragraph (1) the information required under such paragraph, as amended by subparagraphs (A) and (B) of paragraph (1) of this Act; and\n**(B)**\nin the database described such paragraph (2) the information required under such paragraph, as amended by subparagraphs (A) and (C) of paragraph (1) of this Act.\nIII\nCommercialization Improvements\n#### 301. Phase III award education\nSection 9(r) of the Small Business Act ( 15 U.S.C. 638(r) ) is amended by adding at the end the following new paragraph:\n(5) Workforce training (A) In general The Administrator, in coordination with the Secretary of Defense, the Administrator of the General Services Administration, and the head of any such other Federal agency that the Administrator determines appropriate, shall establish training activities for contracting officers and agency acquisition workforce of Federal agencies to ensure that such individuals are fully aware of all aspects of Phase III acquisitions under the SBIR and STTR programs, as applicable. (B) Training topics The training activities required under subparagraph (A) shall include training on\u2014 (i) the missions, goals, and authorities of the SBIR and STTR programs; (ii) the use of Phase III agreement; (iii) Phase III data rights; and (iv) the execution of Phase III sole source award contracts. (C) Definitions In this paragraph: (i) Agency acquisition workforce The term agency acquisition workforce means the employees of a Federal agency that have procurement or acquisition responsibilities, including\u2014 (I) employees described in section 1703 of title 41, United States Code; and (II) individuals that are part of the acquisition workforce (as such term is defined in section 101(a) of title 10, United States Code). (ii) Phase III acquisition The term Phase III acquisition means the acquisition of a good or service from a participant in Phase III that such participant has commercialized or is seeking to commercialize as such a participant. .\n#### 302. Technology Commercialization Official\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by section 204, is further amended by adding at the end the following new subsection:\n(bbb) Technology Commercialization Official The head of each Federal agency required to establish an SBIR or STTR program shall\u2014 (1) designate an existing official within such Federal agency as the Technology Commercialization Official of such Federal agency, who shall\u2014 (A) have sufficient experience with commercialization; (B) provide guidance to recipients of SBIR or STTR awards on commercializing and transitioning technologies; (C) coordinate with the Administrator and the Technology Commercialization Officials of other Federal agencies to identify additional markets and commercialization pathways for promising SBIR and STTR program technologies; (D) submit to the Administrator an annual report on the number of technologies from such SBIR or STTR program that have advanced commercialization activities, including the relevant information required in the commercialization impact assessment report under subsection (ccc); (E) identify and advocate for SBIR and STTR technologies with sufficient technology and commercialization readiness to advance to Phase III awards or other non-SBIR or STTR program contracts; (F) submit to the Administrator an annual report on\u2014 (i) the actions taken by such Federal agency to simply, standardize, and expedite the application process and requirements, procedures, and contracts as required under subsection (hh); and (ii) the results of the actions taken under clause (i); and (G) carry out such other duties as the head of such Federal agency determines necessary; or (2) identify an official in such Federal agency carrying out responsibilities that are substantially similar to those described in subparagraphs (A) through (F) of paragraph (1). .\n#### 303. Phase III improvements\n##### (a) Procurement center representative directives\n**(1) In general**\nSection 9(j)(4) of the Small Business Act ( 15 U.S.C. 638(j)(4) ) is amended by inserting before the period at the end the following: , and advocate for the maximum practicable use and transition of products, services, and technologies developed under SBIR or STTR programs to Phase III by means of Phase III awards to small business concerns .\n**(2) Modification deadline**\nNot later than one year after the date of the enactment of this Act, the Administrator of the Small Business Administration shall modify the policy directives issues pursuant to subsection (j) of section 9 of the Small Business Act ( 15 U.S.C. 638(j) ) in accordance with paragraph (4) of such subsection, as amended by paragraph (1).\n##### (b) Phase III award simplification\nSection 9(r)(4) of the Small Business Act ( 15 U.S.C. 638(r)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraphs:\n(C) report to the Administrator on the actions taken by the Federal agency or Federal prime contractor to develop simplified and standardized procedures and model contracts for Phase I, Phase II, and Phase III SBIR awards; and (D) shall issue standardized solicitation provisions and contract clauses which provide clear guidance on the information that small business concerns participating in SBIR or STTR programs can be expected to provide as part of market research or as part of a proposal by such small business concern to establish eligibility for Phase III awards. .\nIV\nPilot Programs\n#### 401. Extend and modify assistance for administrative, oversight, and contract processing costs\n##### (a) In general\nSection 9(mm) of the Small Business Act ( 15 U.S.C. 638(mm) ), as amended by section 202, is further amended\u2014\n**(1)**\nby designating the text of paragraph (1) as subparagraph (A); and\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (L) as clauses (i) through (xii), respectively;\n**(B)**\nby striking September 30, 2025 and inserting September 30, 2030 ;\n**(C)**\nby striking 3 percent and inserting 3.3 percent ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(B) Transfer of funds (i) In general Not later than 2 months after the date of the enactment of an Act providing appropriations for the Department of Defense, the Department of Energy, the Department of Health and Human Services, the National Aeronautics and Space Administration, or the National Science Foundation, the head of each such entity for which such Act provided appropriations shall transfer not less than 10 percent of the amount of the funds used for the purposes described in clauses (i) through (xii) of subparagraph (A) to the Administrator to increase the resources of the Administration for administering the SBIR and STTR programs. (ii) Fund use limits None of the funds transferred under clause (i) may be used for or with respect to any program established under the Small Business Investment Act of 1958 ( 15 U.S.C. 661 et seq. ). .\n##### (b) Increasing participation of underserved populations in the SBIR and STTR programs\n**(1) In general**\nSection 9(mm)(2) of the Small Business Act ( 15 U.S.C. 638(mm)(2) ) is amended to read as follows:\n(2) Outreach and technical assistance A Federal agency participating in the program under this subsection may use a portion of the funds authorized for uses under paragraph (1) to carry out the policy directive required under subsection (j)(2)(F) and to increase the participation of States with respect to which a low level of SBIR awards have historically been awarded. .\n**(2) Conforming amendment**\nSection 9(mm)(6) of the Small Business Act ( 15 U.S.C. 638(mm)(6) ) is amended by striking including and all that follows and inserting the following:\nincluding\u2014 (A) the use of funds transferred under subparagraph (B) of paragraph (1) for the uses authorized in such subparagraph and to achieve the objectives of paragraph (2); and (B) the use of other funds under this subsection to achieve such objectives. .\n#### 402. Extend and expand the direct to Phase II authority\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nby designating the text of subsection (cc) as paragraph (1); and\n**(2)**\nin subsection (cc)\u2014\n**(A)**\nby striking 2012 through 2025 and inserting 2012 through 2030 ;\n**(B)**\nby striking the National Institutes of Health, the Department of Defense, and the Department of Education may each and inserting each Federal agency required to carry out an SBIR program may ; and\n**(C)**\nby adding at the end the following new paragraphs:\n(2) Limitation The total value of awards provided by a Federal agency under this subsection in a fiscal year shall be\u2014 (A) except as provided in subparagraph (B), not more than 10 percent of the total funds allocated to the SBIR program of the Federal agency during that fiscal year; and (B) with respect to the National Institutes of Health, not more than 15 percent of the total funds allocated to the SBIR program of the National Institutes of Health during that fiscal year. (3) Report Each head of a Federal agency that exercises the authority under this subsection shall include in the next report submitted by such Federal agency under (g)(9) following such exercise the number and amount of awards provided under this subsection by such Federal agency in the period covered by such report. .\n#### 403. Extend commercialization readiness program for civilian agencies\nSection 9(gg) of the Small Business Act ( 15 U.S.C. 638(gg) ) is amended\u2014\n**(1)**\nin the heading, by striking Pilot and inserting Civilian agencies commercialization readiness ;\n**(2)**\nby striking pilot program each place it appears and inserting covered program ; and\n**(3)**\nby striking fiscal year 2025 and inserting fiscal year 2030 .\n#### 404. Extension of certain SBIR and STTR pilot programs\n##### (a) Phase 0 proof of concept partnership program\nSection 9(jj)(7) of the Small Business Act ( 15 U.S.C. 638(jj)(7) ) is amended by striking at the end of fiscal year 2025 and inserting on September 30, 2030 .\n##### (b) Commercialization assistance pilot programs\nSection 9(uu)(3) of the Small Business Act ( 15 U.S.C. 638(uu)(3) ) is amended by striking September 30, 2025 and inserting September 30, 2030 .\n#### 405. Extension of due diligence program to assess security risks\nSection 9(vv)(3)(C) of the Small Business Act ( 15 U.S.C. 638(vv)(3)(C) ) is amended by striking September 30, 2025 and inserting September 30, 2030 .\nV\nOversight and Simplification Initiatives\n#### 501. Annual reports to Congress\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin subsection (g)(9)\u2014\n**(A)**\nby inserting the House Committee on Small Business, Senate Committee on Small Business and Entrepreneurship, after SBIR program to ;\n**(B)**\nby inserting a comma after Administration ; and\n**(C)**\nby inserting after Technology Policy the following: and publish such report on the website of such Federal agency as soon as practicable ;\n**(2)**\nin subsection (o)(10)\u2014\n**(A)**\nby inserting House Committee on Small Business, Senate Committee on Small Business and Entrepreneurship, after STTR program to ;\n**(B)**\nby inserting a comma after Administration ; and\n**(C)**\nby inserting after Technology Policy the following: and publish such report on the website of such Federal agency as soon as practicable ; and\n**(3)**\nin subsection (gg)(6), by inserting Congress and after agency to .\n#### 502. Comptroller General report on diversification and commercialization\n##### (a) In general\nNot later than three years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report on the effectiveness of the SBIR and STTR programs with respect to diversification of participants and commercialization.\n##### (b) Contents\nThe report shall include, to the extent practicable, an assessment of\u2014\n**(1)**\nthe demographics of small business concerns receiving SBIR or STTR awards, including new entrants and underrepresented groups;\n**(2)**\nthe efforts of participating agencies to broaden representation and participation of new entrants and underrepresented groups in the SBIR and STTR programs;\n**(3)**\nhow participating agencies develop solicitation topics and attract applicants;\n**(4)**\nthe efforts of participating agencies to support technology commercialization;\n**(5)**\nthe extent to which the SBIR and STTR awards made by each participating agency align with the research priorities and technology needs of that participating agency; and\n**(6)**\nsuch other matters as the Comptroller General, in consultation with the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives, determines appropriate.\n##### (c) Definitions\nIn this section:\n**(1) Federal agency; sbir; sttr**\nThe terms Federal agency , SBIR , and STTR have the meanings given such terms in section 9(e) of the Small Business Act ( 15 U.S.C. 638(e) ).\n**(2) New entrant**\nThe term new entrant means a small business concern that has not previously received an SBIR or STTR award.\n**(3) Underrepresented groups**\nThe term underrepresented groups means small business concerns located in States with respect to which a low level of SBIR and STTR awards have historically been awarded, small business concerns owned and controlled by women, and small business concerns owned and controlled by socially and economically disadvantaged individuals.\n**(4) Participating agency**\nThe term participating agency means a Federal agency carrying out an SBIR or STTR program under section 9 of the Small Business Act ( 15 U.S.C. 638 ).\n**(5) Small business concern**\nThe term small business concern has the meaning given such term under section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n**(6) Small business concern owned and controlled by socially and economically disadvantaged individuals; small business concern owned and controlled by women**\nThe terms small business concern owned and controlled by socially and economically disadvantaged individuals and small business concern owned and controlled by women have the meanings given such terms in section 8(d) of the Small Business Act ( 15 U.S.C. 637(d) ).\n#### 503. Extend the report on award timeliness\nSection 9(ii)(2)(A) of the Small Business Act ( 15 U.S.C. 638(ii)(2)(A) ) is amended\u2014\n**(1)**\nin the matter preceding clause (i), by striking 3 years and inserting 11 years ;\n**(2)**\nin clause (i), by striking and at the end;\n**(3)**\nby redesignating clause (ii) as clause (iii); and\n**(4)**\nby inserting after clause (i) the following new clause:\n(ii) provides the average and median amount of time that each Federal agency with an SBIR or STTR program takes to review and make a final decision on proposals submitted under the program; and .\n#### 504. Pilot program to accelerate National Institutes of Health evaluation process\n##### (a) In general\nSection 9(hh) of the Small Business Act ( 15 U.S.C. 638(hh) ) is amended by adding at the end the following new paragraph:\n(3) Pilot program to accelerate the national institutes of health sbir and sttr awards (A) In general Not later than 1 year after the date of the enactment of this paragraph, the Director of the National Institutes of Health shall establish a pilot program to reduce the time for awards under the SBIR and STTR programs of the National Institutes of Health. (B) Award procedures In carrying out the pilot program under subparagraph (A), the Director shall develop simplified and standardized procedures across all relevant awarding offices at the National Institutes of Health and reduce the amount of time between the provision of notice of such awards and the subsequent release of funding with respect to the awards to be as close to 90 days as possible. (C) Merit review (i) In general Under the pilot program under subparagraph (A), the Director of the National Institutes of Health may, with respect to awards under the SBIR and STTR programs of the National Institutes of Health, use such peer review procedures (including consultation with appropriate scientific experts) as the Director determines to be appropriate to obtain assessments of scientific and technical merit and potential for commercialization. (ii) Deemed The use of peer review procedures under clause (i) shall be deemed to fulfill any requirements applicable to the award under the SBIR or STTR program of the National Institutes of Health under sections 406(a)(3)(A) and 492 of the Public Health Service Act ( 42 U.S.C. 284a(a)(3)(A) ; 289a). (D) Termination The pilot program under subparagraph (A) shall terminate on September 30, 2030. .\n##### (b) Evaluation report\nNot later than three years after the date of enactment of this Act, the Director of the National Institutes of Health shall submit to the Committees on Small Business and Science, Space, and Technology of the House of Representatives and the Committee on Small Business and Entrepreneurship of the Senate an evaluation of the pilot program established under paragraph (3) of section 9(hh) of the Small Business Act ( 15 U.S.C. 638(hh) ), as added by subsection (a), including an analysis of the peer review procedures used under subparagraph (C) of such paragraph and the effects on award times.\n#### 505. Codifying safeguards for small business concerns majority-owned by venture capital operating companies, hedge funds, or private equity firms\n##### (a) In general\nSection 9(dd) of the Small Business Act ( 15 U.S.C. 638(dd) ) is amended\u2014\n**(1)**\nin paragraph (6)(B), by striking If a Federal and inserting Except as provided in paragraph (8), if a Federal ; and\n**(2)**\nby adding at the end the following new paragraph:\n(8) Participation limits (A) In general A small business concern that is majority-owned by multiple venture capital operating companies, hedge funds, or private equity firms is ineligible to receive an award under any SBIR program if the Administrator determines that such small business concern is, or is owned and controlled in majority part by, a covered foreign entity. (B) Ownership determination In determining whether a small business concern is ineligible to receive an award under any SBIR program under subparagraph (A), the Administrator shall consider whether the small business concern is a direct or indirect subsidiary of a foreign-owned firm. (C) Size standards The Administrator shall establish size standards for small business concerns seeking to participate in an SBIR program solely under the authority under this section. (D) Definitions In this paragraph: (i) Covered foreign entity the term covered foreign entity \u2014 (I) means\u2014 (aa) a foreign entity of concern; (bb) a government or political party of a foreign country of concern; (cc) a natural person who is not a lawful permanent resident of the United States, citizen of the United States, or any other protected individual (as such term is defined in section 274B(a)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324b(a)(3) )); or (dd) a partnership, association, corporation, organization, or other combination of persons organized under the laws of or having its principal place of business in a foreign country of concern; and (II) includes\u2014 (aa) any entity owned by, controlled by, or subject to the jurisdiction or direction of a an entity listed in subclause (I); (bb) any person, wherever located, who acts as an agent, representative, or employee of an entity listed in subclause (I); (cc) any person who acts in any other capacity at the order, request, or under the direction or control, of an entity listed in subclause (I), or of a person whose activities are directly or indirectly supervised, directed, controlled, financed, or subsidized in whole or in majority part by an entity listed in subclause (I); (dd) any person who directly or indirectly through any contract, arrangement, understanding, relationship, or otherwise, owns 25 percent or more of the equity interests of an entity listed in subclause (I); (ee) any person with significant responsibility to control, manage, or direct an entity listed in subclause (I); (ff) any person, wherever located, who is a citizen or resident of a country controlled by an entity listed in subclause (I); or (gg) any corporation, partnership, association, or other organization organized under the laws of a country controlled by an entity listed in subclause (I). (ii) Foreign entity of concern The term foreign entity of concern means a foreign entity that is\u2014 (I) designated as a foreign terrorist organization by the Secretary of State under section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ); (II) included on the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury (commonly known as the SDN list); (III) owned by, controlled by, or subject to the jurisdiction or direction of a government of a foreign country that is a covered nation (as such term is defined in section 4872 of title 10, United States Code); (IV) alleged by the Attorney General to have been involved in activities for which a conviction was obtained under\u2014 (aa) chapter 37 of title 18, United States Code (commonly known as the Espionage Act); (bb) section 951 or 1030 of such title; (cc) chapter 90 of such title (commonly known as the Economic Espionage Act of 1996); (dd) the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ); (ee) section 224, 225, 226, 227, or 236 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2274 , 2275, 2276, 2277, and 2284); (ff) the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ); or (gg) the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); or (V) determined by the Secretary of Commerce, in consultation with the Secretary of Defense and the Director of National Intelligence, to be engaged in unauthorized conduct that is detrimental to the national security or foreign policy of the United States. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply only with respect to awards made under an Small Business Innovation Research Program (as defined in section 9(e) of the Small Business Act ( 15 U.S.C. 638(e) )) after the date of the enactment of this Act.\n#### 506. Commercialization impact assessment\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is further amended by adding at the end the following new subsection:\n(ccc) Commercialization impact assessment (1) In general The Administrator, shall coordinate with the head of each Federal agency with an SBIR or STTR program to develop an annual commercialization impact assessment, which shall measure, for each small business concern that has received not less than 50 Phase II on or after October 1 of the ninth full fiscal year beginning before the fiscal year in which the assessment is carried out\u2014 (A) the total dollar value of Federal awards, including subgrants, contracts, and subcontracts, other than SBIR or STTR awards, received by the small business concern in the preceding 9 fiscal years; (B) the total dollar value of all SBIR and STTR Phase I and Phase II awards received by the small business concern in the preceding 9 fiscal years; (C) the average annual gross revenue of the small business concern over the preceding 9 fiscal years; (D) the total revenue of the small business concern received or realized in the preceding 9 fiscal years from the sale or licensing of any product or service resulting from research conduct under an SBIR or STTR award, disaggregated by the revenue from such sales and the revenue from such licensing; (E) additional investments in the small business concern from any source, other than a Phase I or Phase II SBIR or STTR awards, to further the research and development conducted under an SBIR or STTR award received by the small business concern in the preceding 9 fiscal years; (F) any mergers and acquisitions of SBIR or STTR award recipients during or after the completion of a Phase II award; (G) any new, unique spin-out companies and third party revenues from any business in the preceding 9 fiscal years resulting from research conducted by the small business concern under an SBIR or STTR award; (H) the year in which the first Phase II award was received by the small business concern and the total number of employees of the small business concern at the time of first Phase II award; (I) the number of employees, as of the end of the most recently completed fiscal year; and (J) the total number and value of Phase III awards received by the small business concern. (2) Publication The Administrator shall create a report on the findings of each commercialization impact assessment and shall\u2014 (A) include such report in the annual report required under subsection (b)(7); and (B) submit such report to\u2014 (i) the Committee on Small Business and Entrepreneurship of the Senate; and (ii) the Committees on Science, Space, and Technology and on Small Business of the House of Representatives. .\nVI\nTechnical Changes\n#### 601. Inclusion of SBICs in the SBIR and STTR programs\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by section 505, is further amended\u2014\n**(1)**\nby striking or private equity firm investment each place that term appears and inserting private equity firm, or SBIC investment ;\n**(2)**\nby striking or private equity firms each place that term appears and inserting private equity firms, or SBICs ;\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (18), by striking and at the end;\n**(B)**\nin paragraph (19), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(20) the term SBIC means a small business investment company as defined in section 103 of the Small Business Investment Act of 1958 ( 15 U.S.C. 662 ). ; and\n**(4)**\nin the heading for subsection (dd), by striking or Private Equity Firms and inserting Private Equity Firms, or SBICs .\n#### 602. Phase III and sole-source awards\nSection 9(r) of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin the heading, by inserting Sole Source and Other after Justification for ; and\n**(2)**\nin the heading for paragraph (4), by inserting sole source and other after justification for .",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-09-08",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5212",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Innovation Workforce Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-22",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7217",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR Administrative Funding Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-17",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4520",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Application Assistance Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-25",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4775",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Foreign Interference Safeguard Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4842",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR Commercialization Improvement Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-19",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5001",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Oversight Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "1573",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Reauthorization Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-09",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3851",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Pilot Extension Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-12",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3953",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SBIR/STTR Website Improvement Act",
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
        "name": "Commerce",
        "updateDate": "2025-05-28T13:37:23Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3169ih.xml"
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
      "title": "SBIR/STTR Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SBIR/STTR Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to reauthorize and modify the Small Business Innovation Research and Small Business Technology Transfer Research programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:26Z"
    }
  ]
}
```
