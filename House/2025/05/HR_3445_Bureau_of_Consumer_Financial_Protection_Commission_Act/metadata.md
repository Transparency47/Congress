# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3445?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3445
- Title: Bureau of Consumer Financial Protection Commission Act
- Congress: 119
- Bill type: HR
- Bill number: 3445
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-18T16:07:54Z
- Update date including text: 2026-05-18T16:07:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3445",
    "number": "3445",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Bureau of Consumer Financial Protection Commission Act",
    "type": "HR",
    "updateDate": "2026-05-18T16:07:54Z",
    "updateDateIncludingText": "2026-05-18T16:07:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:05:15Z",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WI"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3445ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3445\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Huizenga (for himself, Mr. Barr , Mr. Meuser , Mr. Fitzgerald , Mr. Rose , Mr. Moore of North Carolina , and Mr. Timmons ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Consumer Financial Protection Act of 2010 to make the Bureau of Consumer Financial Protection an independent agency led by a commission, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bureau of Consumer Financial Protection Commission Act .\n#### 2. Making the Bureau an independent agency led by a commission\nThe Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 et seq. ) is amended\u2014\n**(1)**\nin section 1011\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking in the Federal Reserve System, ; and\n**(ii)**\nby striking independent bureau and inserting independent agency ;\n**(B)**\nby striking subsections (b), (c), and (d);\n**(C)**\nby redesignating subsection (e) as subsection (j);\n**(D)**\nin subsection (j), as so redesignated, by striking , including in cities in which the Federal reserve banks, or branches of such banks, are located, ; and\n**(E)**\nby inserting after subsection (a) the following new subsections:\n(b) Authority To prescribe regulations The commission of the Bureau may prescribe such regulations and issue such orders in accordance with this title as the Bureau may determine to be necessary for carrying out this title and all other laws within the Bureau\u2019s jurisdiction and shall exercise any authorities granted under this title and all other laws within the Bureau\u2019s jurisdiction. (c) Composition of the commission (1) In general The management of the Bureau shall be vested in a commission, which shall be composed of 5 members who shall be appointed by the President, by and with the advice and consent of the Senate, and\u2014 (A) at least 2 of whom shall have private sector experience in the provision of consumer financial products and services; and (B) at least 1 of whom shall have been employed as a State bank supervisor (as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1803 )). (2) Staggering The members of the commission shall serve staggered terms, which initially shall be established by the President for terms of 1, 2, 3, 4, and 5 years, respectively. (3) Terms (A) In general Except with respect to the initial staggered terms described under paragraph (2), each member of the commission, including the Chair, shall serve for a term of 5 years. (B) Removal The President may remove any member of the commission for inefficiency, neglect of duty, or malfeasance in office. (C) Vacancies Any member of the commission appointed to fill a vacancy occurring before the expiration of the term to which that member\u2019s predecessor was appointed (including the Chair) shall be appointed only for the remainder of the term. (D) Continuation of service Each member of the commission may continue to serve after the expiration of the term of office to which that member was appointed until a successor has been appointed by the President and confirmed by the Senate, except that a member may not continue to serve more than 1 year after the date on which that member\u2019s term would otherwise expire. (E) Other employment prohibited No member of the commission shall engage in any other business, vocation, or employment. (d) Affiliation Not more than 3 members of the commission shall be members of any one political party. (e) Chair of the commission (1) Initial Chair The first member and Chair of the commission shall be the individual serving as Director of the Bureau of Consumer Financial Protection on the day before the date of the enactment of this subsection. Such individual shall serve until the President has appointed all 5 members of the commission in accordance with subsection (c). (2) Subsequent Chair Of the 5 members appointed in accordance with subsection (c), the President shall appoint 1 member to serve as the subsequent Chair of the commission. (3) Authority The Chair shall be the principal executive officer of the commission, and shall exercise all of the executive and administrative functions of the commission, including with respect to\u2014 (A) the appointment and supervision of personnel employed under the commission (other than personnel employed regularly and full time in the immediate offices of members of the commission other than the Chair); (B) the distribution of business among personnel appointed and supervised by the Chair and among administrative units of the commission; and (C) the use and expenditure of funds. (4) Limitation In carrying out any of the Chair\u2019s functions under the provisions of this subsection, the Chair shall be governed by general policies of the commission and by such regulatory decisions, findings, and determinations as the commission may by law be authorized to make. (5) Requests or estimates related to appropriations Requests or estimates for regular, supplemental, or deficiency appropriations on behalf of the commission may not be submitted by the Chair without the prior approval of the commission. (6) Designation The Chair shall be known as both the Chair of the commission of the Bureau and the Chair of the Bureau . (f) Initial quorum established For the 6 month period beginning on the date of enactment of this subsection, the first member and Chair of the commission described under subsection (e)(1) shall constitute a quorum for the transaction of business until the President has appointed all 5 members of the commission in accordance with subsection (c). Following such appointment of 5 members, the quorum requirements of subsection (g) shall apply. (g) No impairment by reason of vacancies No vacancy in the members of the commission after the establishment of an initial quorum under subsection (f) shall impair the right of the remaining members of the commission to exercise all the powers of the commission. Three members of the commission shall constitute a quorum for the transaction of business, except that if there are only 3 members serving on the commission because of vacancies in the commission, 2 members of the commission shall constitute a quorum for the transaction of business. If there are only 2 members serving on the commission because of vacancies in the commission, 2 members shall constitute a quorum for the 6-month period beginning on the date of the vacancy which caused the number of commission members to decline to 2. (h) Seal The Bureau shall have an official seal. (i) Compensation (1) Chair The Chair shall receive compensation at the rate prescribed for level I of the Executive Schedule under section 5313 of title 5, United States Code. (2) Other members of the commission The 4 other members of the commission shall each receive compensation at the rate prescribed for level II of the Executive Schedule under section 5314 of title 5, United States Code. ;\n**(2)**\nin section 1012(c)\u2014\n**(A)**\nin the heading, by striking Autonomy of the Bureau and inserting Coordination with the Board of Governors ;\n**(B)**\nby striking (1) Coordination with the board of governors.\u2014 ; and\n**(C)**\nby striking paragraphs (2), (3), (4), and (5); and\n**(3)**\nin section 1014(b), by striking Not fewer than 6 members shall be appointed upon the recommendation of the regional Federal Reserve Bank Presidents, on a rotating basis. and inserting Not fewer than half of all members shall have private sector experience in the provision of consumer financial products and services. .\n#### 3. Deeming of name\nAny reference in a law, regulation, document, paper, or other record of the United States to the Director of the Bureau of Consumer Financial Protection, except in subsection (e)(1) of section 1011 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5491 ), as added by this Act, shall be deemed a reference to the commission leading and governing the Bureau of Consumer Financial Protection, as described under section 1011 of the Consumer Financial Protection Act of 2010.\n#### 4. Conforming amendments\n##### (a) Consumer Financial Protection Act of 2010\n**(1) In general**\nExcept as provided under paragraph (2), the Consumer Financial Protection of 2010 ( 12 U.S.C. 5481 et seq. ) is amended\u2014\n**(A)**\nby striking Director of the Bureau each place such term appears, other than where such term is used to refer to a Director other than the Director of the Bureau of Consumer Financial Protection, and inserting Bureau ;\n**(B)**\nby striking Director each place such term appears and inserting Bureau , other than where such term is used to refer to a Director other than the Director of the Bureau of Consumer Financial Protection; and\n**(C)**\nin section 1002, by striking paragraph (10).\n**(2) Exceptions**\n**(A) In general**\nThe Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 et seq. ) is amended\u2014\n**(i)**\nin section 1013(c)(3)\u2014\n**(I)**\nby striking Assistant Director of the Bureau for and inserting Head of the Office of ; and\n**(II)**\nin subparagraph (B), by striking Assistant Director and inserting Head of the Office ;\n**(ii)**\nin section 1013(g)(2)\u2014\n**(I)**\nby striking Assistant director and inserting Head of the Office ; and\n**(II)**\nby striking an assistant director and inserting a Head of the Office of Financial Protection for Older Americans ;\n**(iii)**\nin section 1016(a), by striking Director of the Bureau and inserting Chair of the Bureau ; and\n**(iv)**\nby striking section 1066.\n**(B) Clerical amendment**\nThe table of contents for the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended by striking the item relating to section 1066.\n##### (b) Dodd-Frank Wall Street Reform and Consumer Protection Act\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 111(b)(1)(D), by striking Director and inserting Chair ; and\n**(2)**\nin section 1447, by striking Director of the Bureau each place such term appears and inserting Chair of the Bureau .\n##### (c) Electronic Fund Transfer Act\nSection 921(a)(4)(C) of the Electronic Fund Transfer Act ( 15 U.S.C. 1693o\u20132(a)(4)(C) ), as added by section 1075(a)(2) of the Consumer Financial Protection Act of 2010, is amended by striking Director of the Bureau of Consumer Financial Protection and inserting Chair of the Bureau of Consumer Financial Protection .\n##### (d) Expedited Funds Availability Act\nThe Expedited Funds Availability Act ( 12 U.S.C. 4001 et seq. ), as amended by section 1086 of the Consumer Financial Protection Act of 2010, is amended by striking Director of the Bureau each place such term appears and inserting Bureau .\n##### (e) Federal Deposit Insurance Act\nSection 2 of the Federal Deposit Insurance Act ( 12 U.S.C. 1812 ), as amended by section 336(a) of the Dodd-Frank Wall Street Reform and Consumer Protection Act, is amended by striking Director of the Consumer Financial Protection Bureau each place such term appears and inserting Chair of the Bureau of Consumer Financial Protection .\n##### (f) Federal Financial Institutions Examination Council Act of 1978\nSection 1004(a)(4) of the Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3303(a)(4) ), as amended by section 1091 of the Consumer Financial Protection Act of 2010, is amended by striking Director of the Consumer Financial Protection Bureau and inserting Chair of the Bureau of Consumer Financial Protection .\n##### (g) Financial Literacy and Education Improvement Act\nSection 513 of the Financial Literacy and Education Improvement Act ( 20 U.S.C. 9702 ), as amended by section 1013(d)(5) of the Consumer Financial Protection Act of 2010, is amended by striking Director each place such term appears and inserting Chair .\n##### (h) Home Mortgage Disclosure Act of 1975\nSection 307 of the Home Mortgage Disclosure Act of 1975 (12 U.S.C. 2806 et seq), as amended by section 1094(6) of the Consumer Financial Protection Act of 2010, is amended by striking Director of the Bureau of Consumer Financial Protection each place such term appears and inserting Bureau of Consumer Financial Protection .\n##### (i) Interstate Land Sales Full Disclosure Act\nThe Interstate Land Sales Full Disclosure Act (15 U.S.C. 1701 et seq), as amended by section 1098A of the Consumer Financial Protection Act of 2010, is amended\u2014\n**(1)**\nin section 1402\u2014\n**(A)**\nby striking paragraph (1); and\n**(B)**\nby redesignating paragraphs (2) through (12) as paragraphs (1) through (11), respectively;\n**(2)**\nin section 1403(c)\u2014\n**(A)**\nby striking him and inserting the Bureau ; and\n**(B)**\nby striking he and inserting the Bureau ;\n**(3)**\nin section 1407\u2014\n**(A)**\nin subsection (c), by striking he and inserting the Bureau ; and\n**(B)**\nin subsection (e), by striking Director or anyone designated by him and inserting Bureau ;\n**(4)**\nin section 1411(a)\u2014\n**(A)**\nby striking his findings and inserting the findings of the Bureau ; and\n**(B)**\nby striking his recommendation and inserting the recommendation of the Bureau ;\n**(5)**\nin section 1415\u2014\n**(A)**\nin subsection (a), by striking he may, in his discretion, and inserting the Bureau may, in the discretion of the Bureau, ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nby striking in his discretion each place such term appears and inserting in the discretion of the Bureau ;\n**(ii)**\nby striking he deems and inserting the Bureau determines ; and\n**(iii)**\nby striking he may deem and inserting the Bureau may determine ; and\n**(C)**\nin subsection (c), by striking the Director, or any officer designated by him, and inserting the Bureau ;\n**(6)**\nin section 1416(a)\u2014\n**(A)**\nby striking Director of the Bureau of Consumer Financial Protection who may delegate any of his and inserting Bureau of Consumer Financial Protection, which may delegate any ;\n**(B)**\nby striking his administrative and inserting administrative ; and\n**(C)**\nby striking himself and inserting the commission of the Bureau ;\n**(7)**\nin section 1418a(b)(4), by striking Secretary\u2019s determination and inserting determination of the Bureau ; and\n**(8)**\nby striking Director each place such term appears and inserting Bureau .\n##### (j) Real Estate Settlement Procedures Act of 1974\nSection 5 of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2604 ), as amended by section 1450 of the Dodd-Frank Wall Street Reform and Consumer Protection Act, is amended\u2014\n**(1)**\nby striking The Director of the Bureau of Consumer Financial Protection (hereafter in this section referred to as the Director ) and inserting The Bureau of Consumer Financial Protection (hereafter in this section referred to as the Bureau ) ; and\n**(2)**\nby striking Director each place such term appears and inserting Bureau .\n##### (k) S.A.F.E. Mortgage Licensing Act of 2008\nThe S.A.F.E. Mortgage Licensing Act of 2008 ( 12 U.S.C. 5101 et seq. ), as amended by section 1100 of the Consumer Financial Protection Act of 2010, is amended\u2014\n**(1)**\nby striking Director each place such term appears in headings and text and inserting Bureau of Consumer Financial Protection ; and\n**(2)**\nin section 1503, by striking paragraph (10).\n##### (l) Title 44, United States Code\nSection 3513(c) of title 44, United States Code, as amended by section 1100D(b) of the Consumer Financial Protection Act of 2010, is amended by striking Director of the .",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-05-29T15:18:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119hr3445",
          "measure-number": "3445",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-15",
          "originChamber": "HOUSE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3445v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bureau of Consumer Financial Protection Commission Act</strong></p><p>This bill restructures the Consumer Financial Protection Bureau (CFPB) and creates a five-member commission to manage the bureau. Currently, the\u00a0CFPB is an autonomous bureau within the Federal Reserve System and is led by a director who is appointed by the President with the advice and consent of the Senate.</p><p>The bill removes the\u00a0CFPB from the Federal Reserve System and reestablishes it as an independent agency.</p><p>The commission established by this bill is composed of five members appointed by the President with the advice and consent of the Senate, with one member selected by the President to serve as chair of the commission. No more than three commissioners may be members of the same political party. The bill also sets forth provisions regarding terms, quorums, and vacancies. The bill specifies that the President may a remove a commissioner for inefficiency, neglect of duty, or malfeasance in office.</p><p>The bill also revises the membership requirements of the Consumer Advisory Board. The board advises and consults with the\u00a0CFPB regarding relevant consumer financial laws and provides information on emerging practices in the consumer financial products and services industry. Currently, at least six members must be appointed upon recommendation of the regional Federal Reserve Bank presidents. The bill removes this requirement and requires at least half of all members to have private sector experience.</p>"
        },
        "title": "Bureau of Consumer Financial Protection Commission Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3445.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Consumer Financial Protection Commission Act</strong></p><p>This bill restructures the Consumer Financial Protection Bureau (CFPB) and creates a five-member commission to manage the bureau. Currently, the\u00a0CFPB is an autonomous bureau within the Federal Reserve System and is led by a director who is appointed by the President with the advice and consent of the Senate.</p><p>The bill removes the\u00a0CFPB from the Federal Reserve System and reestablishes it as an independent agency.</p><p>The commission established by this bill is composed of five members appointed by the President with the advice and consent of the Senate, with one member selected by the President to serve as chair of the commission. No more than three commissioners may be members of the same political party. The bill also sets forth provisions regarding terms, quorums, and vacancies. The bill specifies that the President may a remove a commissioner for inefficiency, neglect of duty, or malfeasance in office.</p><p>The bill also revises the membership requirements of the Consumer Advisory Board. The board advises and consults with the\u00a0CFPB regarding relevant consumer financial laws and provides information on emerging practices in the consumer financial products and services industry. Currently, at least six members must be appointed upon recommendation of the regional Federal Reserve Bank presidents. The bill removes this requirement and requires at least half of all members to have private sector experience.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr3445"
    },
    "title": "Bureau of Consumer Financial Protection Commission Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Consumer Financial Protection Commission Act</strong></p><p>This bill restructures the Consumer Financial Protection Bureau (CFPB) and creates a five-member commission to manage the bureau. Currently, the\u00a0CFPB is an autonomous bureau within the Federal Reserve System and is led by a director who is appointed by the President with the advice and consent of the Senate.</p><p>The bill removes the\u00a0CFPB from the Federal Reserve System and reestablishes it as an independent agency.</p><p>The commission established by this bill is composed of five members appointed by the President with the advice and consent of the Senate, with one member selected by the President to serve as chair of the commission. No more than three commissioners may be members of the same political party. The bill also sets forth provisions regarding terms, quorums, and vacancies. The bill specifies that the President may a remove a commissioner for inefficiency, neglect of duty, or malfeasance in office.</p><p>The bill also revises the membership requirements of the Consumer Advisory Board. The board advises and consults with the\u00a0CFPB regarding relevant consumer financial laws and provides information on emerging practices in the consumer financial products and services industry. Currently, at least six members must be appointed upon recommendation of the regional Federal Reserve Bank presidents. The bill removes this requirement and requires at least half of all members to have private sector experience.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr3445"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3445ih.xml"
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
      "title": "Bureau of Consumer Financial Protection Commission Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Consumer Financial Protection Commission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consumer Financial Protection Act of 2010 to make the Bureau of Consumer Financial Protection an independent agency led by a commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:19Z"
    }
  ]
}
```
