# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6550?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6550
- Title: American FIRST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6550
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 454.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 454.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6550",
    "number": "6550",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "American FIRST Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00454"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 454.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-529.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
        "item": [
          {
            "date": "2026-02-25T18:50:26Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T18:57:42Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T18:57:33Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:01:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "KY"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NE"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TN"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6550ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6550\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Loudermilk (for himself, Mr. Barr , and Mr. Flood ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require annual reporting on interactions between Federal banking supervisory agencies and global financial regulatory or supervisory forums, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Financial Institution Regulatory Sovereignty and Transparency Act of 2025 or the American FIRST Act of 2025 .\n#### 2. Annual reporting on interactions between Federal banking supervisory agencies and global financial regulatory or supervisory forums\n##### (a) Board of Governors of the Federal Reserve System\nThe seventh undesignated paragraph of section 10 of the Federal Reserve Act ( 12 U.S.C. 247 ) is amended\u2014\n**(1)**\nby striking The Board and inserting the following:\n(7) Annual report (A) In general The Board ;\n**(2)**\nby striking the second sentence; and\n**(3)**\nby adding at the end the following:\n(B) Interactions with global financial regulatory or supervisory forums The report required under subparagraph (A) shall include a description of the Board\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (i) a list of the global financial regulatory or supervisory forums in which the Board maintained membership during the period covered by the report; and (ii) for each such global financial regulatory or supervisory forum in the list provided pursuant to clause (i)\u2014 (I) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (II) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this Act and the other Acts that the Board implements; (III) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (IV) a description of the organization the Board maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Board with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (V) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (VI) a description of the positions taken by representatives of the Board at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (VII) a summary of the meetings attended by representatives of the Board at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (VIII) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (IX) a description of any amendments to Federal statutes, regulations of the Board, guidance of the Board, or changes to the Board\u2019s supervisory practices the Board anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (X) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Board during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (XI) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (C) Global financial regulatory or supervisory forum (i) In general In this paragraph, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (I) the Bank for International Settlements; (II) the Basel Committee on Banking Supervision; (III) the Financial Stability Board; (IV) the International Association of Insurance Supervisors; and (V) the Network of Central Banks and Supervisors for Greening the Financial System. (ii) Exception The term global financial regulatory or supervisory forum does not include\u2014 (I) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (II) any international organization with respect to which the Board participates pursuant to a treaty to which the United States is a party. .\n##### (b) Office of the Comptroller of the Currency\n**(1) In general**\nThe second section 333 of the Revised Statutes of the United States ( 12 U.S.C. 14 ; relating to an annual report) is amended to read as follows:\n333. Report of Comptroller (a) In general The Comptroller of the Currency shall make an annual report to Congress. (b) Interactions with global financial regulatory or supervisory forums The report required under subsection (a) shall include a description of the Comptroller\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (1) a list of the global financial regulatory or supervisory forums in which the Comptroller maintained membership during the period covered by the report; and (2) for each such global financial regulatory or supervisory forum in the list provided pursuant to paragraph (1)\u2014 (A) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (B) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this chapter, title LXII, and the other Acts that the Comptroller implements; (C) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (D) a description of the organization the Comptroller maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Office of the Comptroller of the Currency with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (E) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (F) a description of the positions taken by representatives of the Comptroller at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (G) a summary of the meetings attended by representatives of the Comptroller at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (H) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (I) a description of any amendments to Federal statutes, regulations of the Comptroller, guidance of the Comptroller, or changes to the Comptroller\u2019s supervisory practices the Comptroller anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (J) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Comptroller during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (K) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (c) Global financial regulatory or supervisory forum (1) In general In this section, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (A) the Bank for International Settlements; (B) the Basel Committee on Banking Supervision; (C) the Financial Stability Board; (D) the International Association of Insurance Supervisors; and (E) the Network of Central Banks and Supervisors for Greening the Financial System. (2) Exception The term global financial regulatory or supervisory forum does not include\u2014 (A) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (B) any international organization with respect to which the Comptroller participates pursuant to a treaty to which the United States is a party. .\n**(2) Technical correction**\nChapter nine of title VII of the Revised Statutes of the United States is amended\u2014\n**(A)**\nby redesignating the first section 333 ( 12 U.S.C. 14a ; relating to data standards) as section 332;\n**(B)**\nby moving such section so as to appear after section 331; and\n**(C)**\nin the table of contents of such chapter, by amending the item relating to section 332 to read as follows:\n332. DATA STANDARDS; OPEN DATA PUBLICATION. .\n##### (c) Federal Deposit Insurance Corporation\nSection 17(a) of the Federal Deposit Insurance Act ( 12 U.S.C. 1827(a) ) is amended by striking paragraph (3) and inserting the following:\n(3) Interactions with global financial regulatory or supervisory forums The report required under paragraph (1) shall include a description of the Corporation\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (A) a list of the global financial regulatory or supervisory forums in which the Corporation maintained membership during the period covered by the report; and (B) for each such global financial regulatory or supervisory forum in the list provided pursuant to subparagraph (A)\u2014 (i) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (ii) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this Act and the other Acts that the Corporation implements; (iii) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (iv) a description of the organization the Corporation maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Corporation with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (v) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (vi) a description of the positions taken by representatives of the Corporation at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (vii) a summary of the meetings attended by representatives of the Corporation at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (viii) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (ix) a description of any amendments to Federal statutes, regulations of the Corporation, guidance of the Corporation, or changes to the Corporation\u2019s supervisory practices the Corporation anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (x) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Corporation during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (xi) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (4) Global financial regulatory or supervisory forum (A) In general In this subsection, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (i) the Bank for International Settlements; (ii) the Basel Committee on Banking Supervision; (iii) the Financial Stability Board; (iv) the International Association of Insurance Supervisors; and (v) the Network of Central Banks and Supervisors for Greening the Financial System. (B) Exception The term global financial regulatory or supervisory forum does not include\u2014 (i) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (ii) any international organization with respect to which the Corporation participates pursuant to a treaty to which the United States is a party. .\n#### 3. Biannual congressional testimony on interactions with global financial regulatory or supervisory forums\nParagraph (12) of section 10 of the Federal Reserve Act ( 12 U.S.C. 247b ) is amended by inserting before the period at the end the following: and with respect to the conduct of interactions at global financial regulatory or supervisory forums (as defined in paragraph (7)(C)) .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6550rh.xml",
      "text": "IB\nUnion Calendar No. 454\n119th CONGRESS\n2d Session\nH. R. 6550\n[Report No. 119\u2013529]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Loudermilk (for himself, Mr. Barr , and Mr. Flood ) introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Rose , Mr. Sessions , Mr. Davidson , and Mr. Moore of North Carolina\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo require annual reporting on interactions between Federal banking supervisory agencies and global financial regulatory or supervisory forums, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Financial Institution Regulatory Sovereignty and Transparency Act of 2025 or the American FIRST Act of 2025 .\n#### 2. Annual reporting on interactions between Federal banking supervisory agencies and global financial regulatory or supervisory forums\n##### (a) Board of Governors of the Federal Reserve System\nThe seventh undesignated paragraph of section 10 of the Federal Reserve Act ( 12 U.S.C. 247 ) is amended\u2014\n**(1)**\nby striking The Board and inserting the following:\n(7) Annual report (A) In general The Board ;\n**(2)**\nby striking the second sentence; and\n**(3)**\nby adding at the end the following:\n(B) Interactions with global financial regulatory or supervisory forums The report required under subparagraph (A) shall include a description of the Board\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (i) a list of the global financial regulatory or supervisory forums in which the Board maintained membership during the period covered by the report; and (ii) for each such global financial regulatory or supervisory forum in the list provided pursuant to clause (i)\u2014 (I) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (II) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this Act and the other Acts that the Board implements; (III) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (IV) a description of the organization the Board maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Board with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (V) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (VI) a description of the positions taken by representatives of the Board at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (VII) a summary of the meetings attended by representatives of the Board at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (VIII) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (IX) a description of any amendments to Federal statutes, regulations of the Board, guidance of the Board, or changes to the Board\u2019s supervisory practices the Board anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (X) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Board during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (XI) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (C) Global financial regulatory or supervisory forum defined (i) In general In this paragraph, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (I) the Bank for International Settlements; (II) the Basel Committee on Banking Supervision; (III) the Financial Stability Board; (IV) the International Association of Insurance Supervisors; and (V) the Network of Central Banks and Supervisors for Greening the Financial System. (ii) Exception The term global financial regulatory or supervisory forum does not include\u2014 (I) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (II) any international organization with respect to which the Board participates pursuant to a treaty to which the United States is a party. .\n##### (b) Office of the Comptroller of the Currency\n**(1) In general**\nThe second section 333 of the Revised Statutes of the United States ( 12 U.S.C. 14 ; relating to an annual report) is amended to read as follows:\n333. Report of Comptroller (a) In general The Comptroller of the Currency shall make an annual report to Congress. (b) Interactions with global financial regulatory or supervisory forums The report required under subsection (a) shall include a description of the Comptroller\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (1) a list of the global financial regulatory or supervisory forums in which the Comptroller maintained membership during the period covered by the report; and (2) for each such global financial regulatory or supervisory forum in the list provided pursuant to paragraph (1)\u2014 (A) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (B) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this chapter, title LXII, and the other Acts that the Comptroller implements; (C) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (D) a description of the organization the Comptroller maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Office of the Comptroller of the Currency with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (E) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (F) a description of the positions taken by representatives of the Comptroller at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (G) a summary of the meetings attended by representatives of the Comptroller at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (H) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (I) a description of any amendments to Federal statutes, regulations of the Comptroller, guidance of the Comptroller, or changes to the Comptroller\u2019s supervisory practices the Comptroller anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (J) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Comptroller during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (K) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (c) Global financial regulatory or supervisory forum defined (1) In general In this section, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (A) the Bank for International Settlements; (B) the Basel Committee on Banking Supervision; (C) the Financial Stability Board; (D) the International Association of Insurance Supervisors; and (E) the Network of Central Banks and Supervisors for Greening the Financial System. (2) Exception The term global financial regulatory or supervisory forum does not include\u2014 (A) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (B) any international organization with respect to which the Comptroller participates pursuant to a treaty to which the United States is a party. .\n**(2) Technical correction**\nChapter nine of title VII of the Revised Statutes of the United States is amended\u2014\n**(A)**\nby redesignating the first section 333 ( 12 U.S.C. 14a ; relating to data standards) as section 332;\n**(B)**\nby moving such section so as to appear after section 331; and\n**(C)**\nin the table of contents of such chapter, by amending the item relating to section 332 to read as follows:\n332. Data standards; open data publication. .\n##### (c) Federal Deposit Insurance Corporation\nSection 17(a) of the Federal Deposit Insurance Act ( 12 U.S.C. 1827(a) ) is amended by striking paragraph (3) and inserting the following:\n(3) Interactions with global financial regulatory or supervisory forums The report required under paragraph (1) shall include a description of the Corporation\u2019s interactions with global financial regulatory or supervisory forums, including\u2014 (A) a list of the global financial regulatory or supervisory forums in which the Corporation maintained membership during the period covered by the report; and (B) for each such global financial regulatory or supervisory forum in the list provided pursuant to subparagraph (A)\u2014 (i) a description of the general purposes of the global financial regulatory or supervisory forum, including a list of the current members and observers of the global financial regulatory or supervisory forum; (ii) a discussion of how the general purposes of the global financial regulatory or supervisory forum align with the purposes of this Act and the other Acts that the Corporation implements; (iii) an identification of the sources that provided a material amount of funding for the operations of the global financial regulatory or supervisory forum during the period covered by the report; (iv) a description of the organization the Corporation maintained during the period covered by the report to conduct interactions with the global financial regulatory or supervisory forum, including an organizational chart and an identification of the official staff of the Corporation with oversight responsibility for interactions with the global financial regulatory or supervisory forum; (v) a discussion of the financial regulatory or supervisory standard-setting issues under discussion at the global financial regulatory or supervisory forum during the period covered by the report; (vi) a description of the positions taken by representatives of the Corporation at the global financial regulatory or supervisory forum during the period covered by the report, including the rationale, objectives, and potential impacts of such positions; (vii) a summary of the meetings attended by representatives of the Corporation at the global financial regulatory or supervisory forum during the period covered by the report, including a discussion of the key outcomes from such meetings; (viii) the text of any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report, including any implementing material, annex, appendix, side letter, or similar document entered into contemporaneously or in conjunction with the underlying policy, standard, or recommendation, or an identification of a publicly available source for the text of such policy, standard, recommendation, or implementing material; (ix) a description of any amendments to Federal statutes, regulations of the Corporation, guidance of the Corporation, or changes to the Corporation\u2019s supervisory practices the Corporation anticipates will be necessary to implement any final policies, standards, or recommendations adopted by the global financial supervisory or regulatory forum during the period covered by the report; (x) a discussion of rules proposed, rules under consideration, final rules adopted, guidance proposed, guidance under consideration, final guidance adopted, or any other similar actions taken by the Corporation during the period covered by the report to implement agreements of the global financial regulatory or supervisory forum, including an economic impact analysis and a justification for why the expected costs of implementing actions are at least offset by the expected benefits related to economic, national security, financial stability, or other national interests; and (xi) such other information relating to interactions with the global financial regulatory or supervisory forum during the period covered by the report separately requested in writing by the Committee on Banking, Housing, and Urban Affairs of the Senate or the Committee on Financial Services of the House of Representatives. (4) Global financial regulatory or supervisory forum defined (A) In general In this subsection, the term global financial regulatory or supervisory forum means any association or union of nations through or by which two or more foreign authorities engage in some aspect of their conduct of international affairs regarding financial supervision and regulation, including\u2014 (i) the Bank for International Settlements; (ii) the Basel Committee on Banking Supervision; (iii) the Financial Stability Board; (iv) the International Association of Insurance Supervisors; and (v) the Network of Central Banks and Supervisors for Greening the Financial System. (B) Exception The term global financial regulatory or supervisory forum does not include\u2014 (i) international financial institutions, as defined in section 1701(c)(2) of the International Financial Institutions Act ( 22 U.S.C. 262r(c)(2) ); or (ii) any international organization with respect to which the Corporation participates pursuant to a treaty to which the United States is a party. .\n#### 3. Biannual congressional testimony on interactions with global financial regulatory or supervisory forums\nParagraph (12) of section 10 of the Federal Reserve Act ( 12 U.S.C. 247b ) is amended by inserting before the period at the end the following: and with respect to the conduct of interactions at global financial regulatory or supervisory forums (as defined in paragraph (7)(C)) .",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-02-18T15:43:36Z"
          },
          {
            "name": "Business records",
            "updateDate": "2026-02-18T15:51:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-18T15:52:26Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-02-18T15:51:59Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2026-02-18T15:51:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-18T15:53:11Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-18T15:52:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:44:16Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6550ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6550rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "American FIRST Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:19Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "American Financial Institution Regulatory Sovereignty and Transparency Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:19Z"
    },
    {
      "title": "American FIRST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American FIRST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Financial Institution Regulatory Sovereignty and Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require annual reporting on interactions between Federal banking supervisory agencies and global financial regulatory or supervisory forums, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T05:33:31Z"
    }
  ]
}
```
