# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4026
- Title: POST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4026
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-04-20T20:09:52Z
- Update date including text: 2026-04-20T20:09:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4026",
    "number": "4026",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "POST Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-20T20:09:52Z",
    "updateDateIncludingText": "2026-04-20T20:09:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4026ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4026\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 regarding proprietary institutions of higher education in order to protect students and taxpayers.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Students and Taxpayers Act of 2025 or POST Act of 2025 .\n#### 2. 85/15 rule\n##### (a) In general\nSection 102(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (D), by striking and after the semicolon;\n**(B)**\nin subparagraph (E), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(F) meets the requirements of paragraph (2). ;\n**(2)**\nby redesignating paragraph (2) as paragraph (3); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Revenue sources (A) Definitions In this paragraph: (i) Alternative financing arrangement The term alternative financing agreement means a financing agreement between\u2014 (I) a student of an institution; and (II) (aa) the institution; (bb) any entity or individual\u2014 (AA) in the institution's ownership tree; or (BB) with any common ownership of the institution and the entity providing the funds; or (cc) (AA) an entity that has any other relationship or agreement with the institution; or (BB) an entity with common ownership with an entity described in subitem (AA). (ii) Federal education assistance funds The term Federal education assistance funds means Federal funds that are disbursed or delivered to or on behalf of a student to be used to attend such institution, as calculated under subparagraph (C). (B) 85/15 rule In order to qualify as a proprietary institution of higher education under this subsection, an institution shall derive not less than 15 percent of the institution's revenues from sources other than Federal education assistance funds, as calculated in accordance with subparagraphs (A) and (C). (C) Implementation of non-Federal revenue requirement In making calculations under subparagraph (B), an institution of higher education shall\u2014 (i) use the cash basis of accounting; (ii) consider as revenue only those funds generated by the institution from\u2014 (I) tuition, fees, and other institutional charges for students enrolled in programs eligible for assistance under title IV; (II) activities conducted by the institution that are necessary for the education and training of the institution's students, if such activities are\u2014 (aa) conducted on campus or at a facility under the control of the institution; (bb) performed under the supervision of a member of the institution's faculty; (cc) required to be performed by all students in a specific educational program at the institution; and (dd) related directly to services performed by students; (III) a contractual arrangement with a Federal agency for the purpose of providing job training to low-income individuals who are in need of such training; and (IV) funds paid by a student, or on behalf of a student by a party unrelated to the institution, its owners, or affiliates, for an education or training program that is not eligible for assistance under title IV, as long as\u2014 (aa) such noneligible program does not include any courses offered in an eligible program of the proprietary institution; (bb) such noneligible program is provided by the institution, and taught by an instructor of the institution, at\u2014 (AA) its main campus or one of its additional locations, as approved by the appropriate accrediting agency or association; (BB) another school facility approved by the appropriate State agency or accrediting agency or association; or (CC) an employer facility; and (cc) such noneligible program is not a program where the institution is merely providing facilities for test preparation courses, acting as a proctor, or overseeing a course of self-study; (iii) presume that any Federal education assistance funds that are disbursed or delivered to an institution on behalf of a student or directly to a student will be used to pay the student's tuition, fees, or other institutional charges, regardless of whether the institution credits such funds to the student's account or pays such funds directly to the student, except to the extent that the student's tuition, fees, or other institutional charges are satisfied by\u2014 (I) grant funds provided by an outside source that\u2014 (aa) has no affiliation with the institution; and (bb) shares no employees, executives, or board members with the institution; and (II) institutional scholarships described in clause (vi); (iv) include no loans made by an institution of higher education as revenue to the school, except for payments made by current or former students to the institution during the fiscal year for which the determination is being made on such loans that are\u2014 (I) used to satisfy tuition, fees, and other institutional charges; (II) bona fide, as evidenced by standalone repayment agreements between the students and the institution that are enforceable promissory notes; (III) issued at intervals related to the institution's enrollment periods; (IV) subject to regular loan repayments and collections by the institution; and (V) separate from the enrollment contracts signed by the students; (v) include funds from an income share agreement, or any other alternative financing agreement, with a student only if\u2014 (I) the institution clearly identifies the student's institutional charges, and such charges are the same or less than the stated rate for institutional charges; (II) the agreement clearly identifies the maximum time and maximum amount a student would be required to pay, including the implied or imputed interest rate and any fees and revenue generated for a related third party, the institution, or an entity described in subparagraph (A)(i)(II), for that maximum time period; and (III) all payments under the agreement are applied with a portion allocated to the return of capital and a portion allocated to profit, with revenue, interest, and fees not included in the calculation; (vi) include a scholarship provided by the institution\u2014 (I) only if the scholarship is in the form of monetary aid based upon the academic achievements or financial need of students, disbursed to qualified student recipients during each fiscal year from an established restricted account; and (II) only to the extent that funds in that account represent designated funds, or income earned on such funds, from an outside source that\u2014 (aa) has no affiliation with the institution; and (bb) shares no employees, executives, or board members with the institution; and (vii) exclude from revenues\u2014 (I) the amount of funds the institution received under part C of title IV, unless the institution used those funds to pay a student's institutional charges; (II) the amount of funds the institution received under subpart 4 of part A of title IV; (III) the amount of funds provided by the institution as matching funds for any Federal program; (IV) the amount of Federal education assistance funds provided to the institution to pay institutional charges for a student that were refunded or returned; and (V) the amount charged for books, supplies, and equipment, unless the institution includes that amount as tuition, fees, or other institutional charges. (D) Regaining eligibility Notwithstanding subparagraph (B), a proprietary institution of higher education that fails to meet the requirements of such subparagraph for a fiscal year shall be ineligible for purposes of this paragraph for a period of not less than 2 institutional fiscal years. To regain eligibility under this paragraph, the proprietary institution shall demonstrate compliance with all eligibility and certification requirements under section 498 for a minimum of 2 institutional fiscal years after the institutional fiscal year in which the institution became ineligible. (E) Report to congress Not later than the third full award year (as defined in section 481(a)(1)) that begins after the date of enactment of the Protecting Our Students and Taxpayers Act of 2025 , and by July 1 of each succeeding year, the Secretary shall submit to the authorizing committees a report that contains, for each proprietary institution of higher education that receives assistance under title IV and as provided in the audited financial statements submitted to the Secretary by each institution pursuant to the requirements of section 487(c)\u2014 (i) the amount and percentage of such institution's revenues received from Federal education assistance funds; and (ii) the amount and percentage of such institution's revenues received from other sources. .\n##### (b) Repeal of existing requirements\nSection 487 of the Higher Education Act of 1965 ( 20 U.S.C. 1094 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (24);\n**(B)**\nby redesignating paragraphs (25) through (29) as paragraphs (24) through (28), respectively;\n**(C)**\nin paragraph (24)(A)(ii) (as redesignated by subparagraph (B)), by striking subsection (e) and inserting subsection (d) ; and\n**(D)**\nin paragraph (26) (as redesignated by subparagraph (B)), by striking subsection (h) and inserting subsection (g) ;\n**(2)**\nby striking subsection (d);\n**(3)**\nby redesignating subsections (e) through (j) as subsections (d) through (i), respectively;\n**(4)**\nin the matter preceding paragraph (1) of subsection (d) (as redesignated by paragraph (3)), by striking (a)(25) and inserting (a)(24) ;\n**(5)**\nin subsection (f)(1) (as redesignated by paragraph (3)), by striking subsection (e)(2) and inserting subsection (d)(2) ; and\n**(6)**\nin subsection (g)(1) (as redesignated by paragraph (3)), by striking subsection (a)(27) in the matter preceding subparagraph (A) and inserting subsection (a)(26) .\n##### (c) Conforming amendments\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended\u2014\n**(1)**\nin section 152 ( 20 U.S.C. 1019a )\u2014\n**(A)**\nin subsection (a)(1)(A), by striking subsections (a)(27) and (h) of section 487 and inserting subsections (a)(26) and (g) of section 487 ; and\n**(B)**\nin subsection (b)(1)(B)(i)(I), by striking section 487(e) and inserting section 487(d) ;\n**(2)**\nin section 153(c)(3) ( 20 U.S.C. 1019b(c)(3) ), by striking section 487(a)(25) each place the term appears and inserting section 487(a)(24) ;\n**(3)**\nin section 496(c)(3)(A) ( 20 U.S.C. 1099b(c)(3)(A) ), by striking section 487(f) and inserting section 487(e) ; and\n**(4)**\nin section 498(k)(1) ( 20 U.S.C. 1099c(k)(1) ), by striking section 487(f) and inserting section 487(e) .\n#### 3. Effective date\n##### (a) In general\nThe amendments made by this Act shall take effect on the second full award year that begins after the date of enactment of this Act.\n##### (b) Award year\nIn this section, the term award year has the meaning given the term in section 481(a)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1088(a)(1) ).",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2107",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "POST Act of 2025",
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
        "name": "Education",
        "updateDate": "2025-07-09T12:44:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-17",
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
          "measure-id": "id119hr4026",
          "measure-number": "4026",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4026v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-06-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Our Students and Taxpayers Act of 2025 or the POST Act of 2025</strong></p><p>This bill requires proprietary (i.e., for-profit) institutions of higher education (IHEs) to derive a larger portion of their revenues from nonfederal\u00a0sources by replacing the existing 90/10 rule with an 85/15 rule.</p><p>Specifically, the bill requires a proprietary IHE to derive at least 15% of its revenue from sources other than federal education assistance funds. (Currently, a proprietary IHE must derive at least 10% of its revenue from sources other than federal education assistance funds.)</p><p>Additionally, the bill specifies how revenue must be calculated for purposes of the 85/15 rule. (Currently, the Higher Education Act of 1965 and accompanying regulatory provisions specify how revenue must be calculated for purposes of the 90/10 rule.)</p><p>Finally, the bill makes a proprietary IHE that fails to meet the 85/15 rule's requirements for a fiscal year ineligible to participate in federal student aid programs for at least two institutional fiscal years. However, the proprietary IHE may regain eligibility if it complies with all eligibility and certification requirements for at least two institutional fiscal years. (Currently, if a proprietary IHE fails to meet the 90/10 rule's requirement in a single year, then its certification to participate in federal student aid programs becomes provisional for two institutional fiscal years. Further, if a\u00a0proprietary IHE fails to meet the rule's requirements in two consecutive years, then it loses its eligibility to participate in these programs for at least two institutional fiscal years.)</p>"
        },
        "title": "POST Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4026.xml",
    "summary": {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Students and Taxpayers Act of 2025 or the POST Act of 2025</strong></p><p>This bill requires proprietary (i.e., for-profit) institutions of higher education (IHEs) to derive a larger portion of their revenues from nonfederal\u00a0sources by replacing the existing 90/10 rule with an 85/15 rule.</p><p>Specifically, the bill requires a proprietary IHE to derive at least 15% of its revenue from sources other than federal education assistance funds. (Currently, a proprietary IHE must derive at least 10% of its revenue from sources other than federal education assistance funds.)</p><p>Additionally, the bill specifies how revenue must be calculated for purposes of the 85/15 rule. (Currently, the Higher Education Act of 1965 and accompanying regulatory provisions specify how revenue must be calculated for purposes of the 90/10 rule.)</p><p>Finally, the bill makes a proprietary IHE that fails to meet the 85/15 rule's requirements for a fiscal year ineligible to participate in federal student aid programs for at least two institutional fiscal years. However, the proprietary IHE may regain eligibility if it complies with all eligibility and certification requirements for at least two institutional fiscal years. (Currently, if a proprietary IHE fails to meet the 90/10 rule's requirement in a single year, then its certification to participate in federal student aid programs becomes provisional for two institutional fiscal years. Further, if a\u00a0proprietary IHE fails to meet the rule's requirements in two consecutive years, then it loses its eligibility to participate in these programs for at least two institutional fiscal years.)</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr4026"
    },
    "title": "POST Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Students and Taxpayers Act of 2025 or the POST Act of 2025</strong></p><p>This bill requires proprietary (i.e., for-profit) institutions of higher education (IHEs) to derive a larger portion of their revenues from nonfederal\u00a0sources by replacing the existing 90/10 rule with an 85/15 rule.</p><p>Specifically, the bill requires a proprietary IHE to derive at least 15% of its revenue from sources other than federal education assistance funds. (Currently, a proprietary IHE must derive at least 10% of its revenue from sources other than federal education assistance funds.)</p><p>Additionally, the bill specifies how revenue must be calculated for purposes of the 85/15 rule. (Currently, the Higher Education Act of 1965 and accompanying regulatory provisions specify how revenue must be calculated for purposes of the 90/10 rule.)</p><p>Finally, the bill makes a proprietary IHE that fails to meet the 85/15 rule's requirements for a fiscal year ineligible to participate in federal student aid programs for at least two institutional fiscal years. However, the proprietary IHE may regain eligibility if it complies with all eligibility and certification requirements for at least two institutional fiscal years. (Currently, if a proprietary IHE fails to meet the 90/10 rule's requirement in a single year, then its certification to participate in federal student aid programs becomes provisional for two institutional fiscal years. Further, if a\u00a0proprietary IHE fails to meet the rule's requirements in two consecutive years, then it loses its eligibility to participate in these programs for at least two institutional fiscal years.)</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr4026"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4026ih.xml"
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
      "title": "POST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Students and Taxpayers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 regarding proprietary institutions of higher education in order to protect students and taxpayers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T11:18:20Z"
    }
  ]
}
```
