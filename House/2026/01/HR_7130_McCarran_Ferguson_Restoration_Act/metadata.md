# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7130
- Title: McCarran-Ferguson Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 7130
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-04-24T08:06:53Z
- Update date including text: 2026-04-24T08:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7130",
    "number": "7130",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "McCarran-Ferguson Restoration Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:53Z",
    "updateDateIncludingText": "2026-04-24T08:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7130ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7130\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Downing (for himself, Mr. Fitzgerald , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo eliminate the Federal Insurance Office of the Department of the Treasury and to establish a United States Insurance Representative within the Department of the Treasury, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the McCarran-Ferguson Restoration Act .\n#### 2. Elimination of Federal Insurance Office\n##### (a) In general\nThe Federal Insurance Office of the Department of the Treasury, and the position of the Director of the Federal Insurance Office, are hereby eliminated.\n##### (b) Treasury authority\nThis section may not be construed to repeal or otherwise limit any authority of the Secretary of the Treasury with respect matters relating to insurance.\n#### 3. Establishment of United States Insurance Representative\nTitle 31, United States Code, is amended\u2014\n**(1)**\nin the table of sections for subchapter I of chapter 3, by striking Federal Insurance Office and inserting United States Insurance Representative ; and\n**(2)**\nby amending section 313 to read as follows:\n313. United States Insurance Representative (a) In general Not later than 1 year after the date of the enactment of this section, the Secretary shall, for the purpose of carrying out this section\u2014 (1) appoint an United States Insurance Representative; and (2) hire and retain individuals with expertise in matters related to insurance. (b) Duties The United States Insurance Representative shall\u2014 (1) coordinate Federal efforts and develop Federal policy on prudential aspects of international insurance matters; (2) represent the United States Department of the Treasury, as appropriate, in the International Association of Insurance Supervisors (or a successor entity); (3) assist the Secretary in negotiating covered agreements; (4) determine whether State insurance measures are preempted by covered agreements; (5) assist the Secretary in administering the Terrorism Insurance Program established in the Department of the Treasury under the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note); (6) consult with the States (including State insurance regulators) with respect to insurance matters of national importance and prudential insurance matters of international importance; and (7) advise the Secretary on prudential international insurance policy issues. (c) Scope The authority of the United States Insurance Representative shall extend to prudential aspects of all lines of insurance offered in the United States, except\u2014 (1) health insurance, as determined by the Secretary in coordination with the Secretary of Health and Human Services based on section 2791 of the Public Health Service Act ( 42 U.S.C. 300gg\u201391 ); (2) long-term care insurance, except long-term care insurance that is included with life or annuity insurance components, as determined by the Secretary in coordination with the Secretary of Health and Human Services, and in the case of long-term care insurance that is included with such components, the Secretary shall coordinate with the Secretary of Health and Human Services in performing the functions under this paragraph; and (3) crop insurance, as established by the Federal Crop Insurance Act (7 U.S.C. 1501 et seq). (d) Preemption of State Insurance Measures (1) Standard A State insurance measure shall be preempted pursuant to this paragraph or section 314 if, and only to the extent that the United States Insurance Representative determines, in accordance with this paragraph, that the measure\u2014 (A) results in less favorable treatment of a non-United States insurer domiciled in a foreign jurisdiction that is subject to a covered agreement than a United States insurer domiciled, licensed, or otherwise admitted in that State; and (B) is inconsistent with a covered agreement. (2) Determination (A) Notice of potential inconsistency Before making any determination under paragraph (1), the United States Insurance Representative shall\u2014 (i) notify and consult with the appropriate State regarding any potential inconsistency or preemption; (ii) notify and consult with the United States Trade Representative regarding any potential inconsistency or preemption; (iii) publish in the Federal Register a notice of the potential inconsistency or preemption, including a description of each State insurance measure at issue and any applicable covered agreement; (iv) provide interested parties a reasonable opportunity to submit written comments to the United States Insurance Representative; and (v) consider any comments received. (B) Scope of review For purposes of this subsection, any determination of the United States Insurance Representative regarding State insurance measures, and any preemption under clause (i) as a result of such determination, shall be limited to the subject matter contained within the covered agreement involved and shall achieve a level of protection for insurance or reinsurance consumers that is substantially equivalent to the level of protection achieved under State insurance or reinsurance regulation. (C) Notice of determination of inconsistency Upon making any determination under paragraph (1), the United States Insurance Representative shall\u2014 (i) notify the appropriate State of the determination and the extent of the inconsistency; (ii) establish a reasonable period of time, which shall not be less than 30 days, before the determination shall become effective; and (iii) notify the Committees on Financial Services and Ways and Means of the House of Representatives and the Committees on Banking, Housing, and Urban Affairs and Finance of the Senate. (3) Notice of effectiveness Upon the conclusion of the period referred to in paragraph (2)(C)(ii), if the basis for such determination still exists, the determination shall become effective and the United States Insurance Representative shall\u2014 (A) publish a notice in the Federal Register that the preemption has become effective, as well as the effective date; and (B) notify the appropriate State of the preemption of the State measure. (4) Limitation No State may enforce a State insurance measure that has been preempted under this subparagraph. (e) Applicability of Administrative Procedures Act Determinations of under subsection (d) shall be subject to the applicable provisions of subchapter II of chapter 5 of title 5, United States Code (relating to administrative procedure), and chapter 7 of such title (relating to judicial review), except that in any action for judicial review of a determination of inconsistency, the court shall determine the matter de novo. (f) Regulations, policies, and procedures The Secretary may issue orders, regulations, policies, and procedures to implement this paragraph. (g) Consultation The United States Insurance Representative shall consult with State insurance regulators, individually or collectively, to the extent the United States Insurance Representative determines appropriate, in carrying out this paragraph. (h) Rules of construction Nothing in this paragraph or section 314 shall be construed to\u2014 (1) alter, amend, or limit any provision of the Consumer Financial Protection Agency Act of 2010; (2) affect the preemption of any State insurance measure otherwise inconsistent with and preempted by Federal law; (3) preempt\u2014 (A) any State insurance measure that governs any insurer\u2019s rates, premiums, underwriting, or sales practices; (B) any State coverage requirements for insurance; (C) the application of the antitrust laws of any State to the business of insurance; or (D) any State insurance measure governing the capital or solvency of an insurer, except to the extent that such State insurance measure results in less favorable treatment of a non-United States insurer than a United States insurer; (4) provide the United States Insurance Representative or the Department of the Treasury with general supervisory or regulatory authority over the business of insurance; (5) limit the authority of any Federal financial regulatory agency, including the authority to develop and coordinate policy, negotiate, and enter into agreements with foreign governments, authorities, regulators, and multinational regulatory committees and to preempt State measures to affect uniformity with international regulatory agreements; or (6) affect the authority of the Office of the United States Trade Representative pursuant to section 141 of the Trade Act of 1974 ( 19 U.S.C. 2171 ) or any other provision of law, including authority over the development and coordination of United States international trade policy and the administration of the United States trade agreements program. (i) Annual report to Congress (1) Preemption reports Beginning on the date that is 2 years after the date of the enactment of this paragraph, and annually thereafter, the United States Insurance Representative shall submit a report to the President and to the Committees on Financial Services and Ways and Means of the House of Representatives and the Committees on Banking, Housing, and Urban Affairs and Finance of the Senate on any actions taken during the preceding 1-year period by the Representative pursuant to subsection (d). (2) International insurance reports Not later than 2 years after the date of the enactment of this paragraph, the United States Insurance Representative shall conduct a study and submit a report to the Congress that describes\u2014 (A) any international coordination of insurance regulation; and (B) the international competitiveness of United States insurers. (j) Use of Existing Resources To carry out this paragraph, the United States Insurance Representative may use personnel, facilities, and any other resource of the Department of the Treasury that are available to the Secretary. (k) Definitions In this paragraph and section 314, the following definitions shall apply: (1) Covered agreement The term covered agreement means a written bilateral or multilateral agreement regarding prudential measures with respect to the business of insurance or reinsurance that\u2014 (A) is entered into between the United States and one or more foreign governments, authorities, or regulatory entities; and (B) relates to the recognition of prudential measures with respect to the business of insurance or reinsurance that achieves a level of protection for insurance or reinsurance consumers that is substantially equivalent to the level of protection achieved under State insurance or reinsurance regulation. (2) Insurer The term insurer means any person engaged in the business of insurance, including reinsurance. (3) Federal financial regulatory agency The term Federal financial regulatory agency means the Department of the Treasury, the Board of Governors of the Federal Reserve System, the Office of the Comptroller of the Currency, the Office of Thrift Supervision, the Securities and Exchange Commission, the Commodity Futures Trading Commission, the Federal Deposit Insurance Corporation, the Federal Housing Finance Agency, or the National Credit Union Administration. (4) Non-united states insurer The term non-United States insurer means an insurer that is organized under the laws of a jurisdiction other than a State, but does not include any United States branch of such an insurer. (5) State insurance measure The term State insurance measure means any State law, regulation, administrative ruling, bulletin, guideline, or practice relating to or affecting prudential measures applicable to insurance or reinsurance. (6) State insurance regulator The term State insurance regulator means any State regulatory authority responsible for the supervision of insurers. (7) Substantially equivalent to the level of protection achieved The term substantially equivalent to the level of protection achieved means the prudential measures of a foreign government, authority, or regulatory entity achieve a similar outcome in consumer protection as the outcome achieved under State insurance or reinsurance regulation. (8) United states insurer The term United States insurer means\u2014 (A) an insurer that is organized under the laws of a State; or (B) a United States branch of a non-United States insurer. .\n#### 4. Related amendments to elimination of Federal Insurance Office\n##### (a) Dodd-Frank Wall Street Reform and Consumer Protection Act amendments\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 165(i) ( 12 U.S.C. 5365(i) )\u2014\n**(A)**\nin paragraph (1)(A), by striking and the Federal Insurance Office and inserting and the Secretary of the Treasury ; and\n**(B)**\nin paragraph (2)(C), in the matter preceding clause (i), by striking and the Federal Insurance Office and inserting and the Secretary of the Treasury ; and\n**(2)**\nin section 203(a)(1)(C) ( 12 U.S.C. 5383(a)(1)(C) ), by striking Director of the Federal Insurance Office in each place it appears and inserting United States Insurance Representative .\n##### (b) Economic Growth, Regulatory Relief, and Consumer Protection Act amendments\nSection 211(a) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 31 U.S.C. 313 note) is amended\u2014\n**(1)**\nin paragraph (1), by striking the Secretary of the Treasury, Board of Governors of the Federal Reserve System, and Director of the Federal Insurance Office and inserting the following: the Secretary of the Treasury and the Board of Governors of the Federal Reserve System ; and\n**(2)**\nin paragraph (2), by striking the Secretary of the Treasury, the Board of Governors of the Federal Reserve System, and the Director of the Federal Insurance Office each place that term occurs and inserting the following: the Secretary of the Treasury and the Board of Governors of the Federal Reserve System .\n#### 5. Financial Stability Oversight Council membership\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 111 ( 12 U.S.C. 5321 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (I), by striking and at the end;\n**(II)**\nin subparagraph (J), by striking the period at the end and inserting ; and ; and\n**(III)**\nby adding at the end the following:\n(K) a State insurance commissioner appointed by the President, by and with the advice and consent of the Senate, as described in paragraph (4). ;\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nin subparagraph (B), to read as follows:\n(B) the United States Insurance Representative; ;\n**(II)**\nby striking subparagraph (C); and\n**(III)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (C) and (D), respectively; and\n**(iii)**\nby adding at the end the following:\n(4) Appointment of State insurance commissioner (A) In general Before making any appointments pursuant to paragraph (1)(K), the President shall request a list of recommended candidates from the States through the National Association of Insurance Commissioners, which shall not be binding on the President. (B) Failure of list submission If the National Association of Insurance Commissioners fails to submit a list of recommendations not later than 15 business days after the date of the request, the President may make the requisite appointment without considering the views of the National Association of Insurance Commissioners. ; and\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nby inserting , the State insurance commissioner shall serve a term of 4 years after 6 years ; and\n**(II)**\nby striking (C), (D), and (E) and inserting (C) and (D) ; and\n**(ii)**\nby adding at the end the following:\n(5) Acting State insurance commissioner may serve (A) In general Notwithstanding section 3345 of title 5, United States Code, in the event of a vacancy of the State insurance commissioner of the Council or during the absence or disability of the State insurance commissioner of the Council, an acting State insurance commissioner of the Council shall serve as a nonvoting member of the Council until a successor is appointed and confirmed. (B) Selection of acting State insurance commissioner The acting State insurance commissioner described in subparagraph (A) shall be selected through process determined by the National Association of Insurance Commissioners. (6) Term of State insurance commissioner Notwithstanding paragraph (1), if a successor to the State insurance commissioner of the Council is not appointed and confirmed by the end of the term of service of the commissioner, such member may continue to serve until the earlier of\u2014 (A) 18 months after the date on which the term of service ends; or (B) the date on which a successor to the commissioner is appointed and confirmed. , and\n**(2)**\nin section 112 ( 12 U.S.C. 5322 )\u2014\n**(A)**\nin subsection (a)(2)(A), by striking member agencies, other Federal and State financial regulatory agencies, the Federal Insurance Office and inserting the following: member agencies and other Federal and State financial regulatory agencies ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking the Office of Financial Research, member agencies, and the Federal Insurance Office and inserting the Office of Financial Research and member agencies ; and\n**(ii)**\nin paragraph (2), by striking , any member agency, and the Federal Insurance Office, and inserting and any member agency .",
      "versionDate": "2026-01-16",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-02-04T19:23:00Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7130ih.xml"
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
      "title": "McCarran-Ferguson Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "McCarran-Ferguson Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To eliminate the Federal Insurance Office of the Department of the Treasury and to establish a United States Insurance Representative within the Department of the Treasury, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:40Z"
    }
  ]
}
```
