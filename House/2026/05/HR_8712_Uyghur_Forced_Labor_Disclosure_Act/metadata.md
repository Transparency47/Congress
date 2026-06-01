# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8712
- Title: Uyghur Forced Labor Disclosure Act
- Congress: 119
- Bill type: HR
- Bill number: 8712
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T18:33:49Z
- Update date including text: 2026-05-21T18:33:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H3461)
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H3461)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8712",
    "number": "8712",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Uyghur Forced Labor Disclosure Act",
    "type": "HR",
    "updateDate": "2026-05-21T18:33:49Z",
    "updateDateIncludingText": "2026-05-21T18:33:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3461)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:01:50Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
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
      "sponsorshipDate": "2026-05-07",
      "state": "IN"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "HI"
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
      "sponsorshipDate": "2026-05-07",
      "state": "DC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MD"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8712ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8712\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Subramanyam (for himself, Mr. Moran , Mr. Carson , Mr. Espaillat , Mr. Krishnamoorthi , Mr. McGovern , Ms. Pelosi , Ms. Titus , Mr. Moulton , Ms. Tokuda , Ms. Norton , Mr. Raskin , and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to require issuers to make certain disclosures relating to the Xinjiang Uyghur Autonomous Region, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uyghur Forced Labor Disclosure Act .\n#### 2. Certification of certain activities relating to the Xinjiang Uyghur Autonomous Region as procedure for registration of securities on an exchange\n##### (a) In general\nSection 12 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l ) is amended by adding at the end the following:\n(m) Reporting of certain activities relating to the Xinjiang Uyghur Autonomous Region (1) In general Not later than the end of the 180-day period beginning on the date of enactment of this subsection, the Commission shall issue rules\u2014 (A) to require an issuer filing an application to register a security with a national securities exchange to\u2014 (i) include in such application the documentation described under paragraph (2); and (ii) to file the application and documentation with the Commission; (B) to require an issuer to file a report with the Commission containing the documentation described under paragraph (2) if the issuer is not listed on an exchange and merges with another issuer that is listed on the exchange; and (C) to require an issuer filing a registration statement under subsection (g) to include with such statement the documentation described under paragraph (2). (2) Documentation required With respect to an issuer, the documentation described under this paragraph is documentation showing whether the issuer or any affiliate of the issuer, directly or indirectly, contains within its supply or production chain\u2014 (A) goods, wares, articles, or merchandise sourced from or through the XUAR, or mined, produced, or manufactured wholly or in part by forced labor identified by mandate of section 2(d)(2)(B)(iv) of Public Law 117\u201378 , including\u2014 (i) the industries contained on the Illustrative List of Industries in Xinjiang in which Public Reporting has indicated Labor Abuses may be Taking Place in Annex 2 of the Xinjiang Supply Chain Business Advisory (published July 13, 2021) and any successor list; and (ii) all products listed within high-priority sectors for enforcement by the Forced Labor Enforcement Task Force pursuant to Public Law 117\u201378 ; or (B) goods, wares, articles, or merchandise that are mined, produced, or manufactured by an entity engaged in labor transfers from the XUAR or forced labor. (3) Transparent documentation of supply chain links In issuing rules under paragraph (1), the Commission shall require an issuer to list the name (in English and in the most commonly spoken language of the country in which the issuer is incorporated, if other than English), address, and sourcing quantities from each smelter, refinery, farm, or manufacturing facility (as appropriate) of each person mining, producing, or manufacturing a good, ware, article, or merchandise described under paragraph (2). (4) Independent verification of documentation In issuing rules under paragraph (1), the Commission shall require an issuer\u2014 (A) to obtain independent verification of the documentation described under paragraph (2), by a third-party auditor approved by the Commission, before the filing of an application, report, or registration statement containing such documentation; (B) to maintain the confidentiality of the identity of such third-party auditor, unless the auditor proactively waives confidentiality; and (C) to establish policies to respond to any reprisals against the third-party auditor. (5) Public availability of documentation The Commission shall make all documentation received under this subsection available to the public. (6) Additional penalties for certain violations In addition to other penalties provided under this Act, with respect to an application described under paragraph (1)(A), if an issuer fails to comply with the requirements of this subsection (including any misrepresentation of the information described under paragraph (3))\u2014 (A) the applicable national securities exchange may not approve such application; and (B) the issuer may not re-file the application for 1 year. (7) Definitions In this subsection: (A) Forced labor The term forced labor means\u2014 (i) any labor carried out by the Uyghur, Kazakh, Kyrgyz, or another oppressed ethnic group in the People\u2019s Republic of China under any State-sponsored labor program, including any program associated with surplus labor transfer , poverty alleviation , mutual aid , Xinjiang Aid , and re-education programs targeting minoritized citizens of the XUAR, whether inside or outside; (ii) any labor carried out in the XUAR unless the specific labor has been identified by the United States authorities under existing forced labor and the Uyghur protection laws as not involving the use of forced labor; and (iii) any use of convict labor, forced labor, or indentured labor described under section 307 of the Tariff Act of 1930 ( 19 U.S.C. 1307 ). (B) XUAR The term XUAR means the Xinjiang Uyghur Autonomous Region. .\n##### (b) Repeal\nThe amendment made by this section shall be repealed on the earlier of\u2014\n**(1)**\nthe date that is 8 years after the date of the enactment of this section; or\n**(2)**\nthe date on which the President submits to Congress (including the Office of the Law Revision Council) a determination that the Government of the People\u2019s Republic of China has ended mass internment, forced labor, and any other gross violations of human rights experienced by Uyghurs, Kazakhs, Kyrgyz, and members of other persecuted groups in the Xinjiang Uyghur Autonomous Region.\n#### 3. Disclosure of certain activities relating to the Xinjiang Uyghur Autonomous Region\n##### (a) In general\nSection 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ) is amended by adding at the end the following:\n(t) Disclosure of certain activities relating to the Xinjiang Uyghur Autonomous Region (1) In general Not later than the end of the 180-day period beginning on the date of enactment of this subsection, the Commission shall issue rules to require each issuer required to file an annual report under this section or section 15(d) or a proxy statement under section 14 to disclose in each such report or proxy statement whether, during the period covered by the report or proxy statement\u2014 (A) the issuer or any affiliate of the issuer, directly or indirectly, engaged with an entity or the affiliate of an entity to use or source goods, wares, articles, or merchandise sourced from or through the XUAR, or mined, produced, or manufactured wholly or in part by forced labor identified by mandate of section 2(d)(2)(B)(iv) of Public Law 117\u201378 , including\u2014 (i) the industries contained on the Illustrative List of Industries in Xinjiang in which Public Reporting has indicated Labor Abuses may be Taking Place in Annex 2 of the Xinjiang Supply Chain Business Advisory (published July 13, 2021) and any successor list; (ii) all products listed as high-priority sectors for enforcement by the Forced Labor Enforcement Task Force pursuant to Public Law 117\u201378 ; and (iii) all products exported from the People\u2019s Republic of China into the United States that are listed by mandate of section 2(d)(2)(B)(iv) of Public Law 117\u201378 that are sourced from or through the XUAR; or (B) with respect to any goods, wares, articles, or merchandise described under subparagraph (A), whether the goods, wares, articles, or merchandise have supply chain links to facilities that employ forced labor; (C) with respect to each good, ware, article, and merchandise described under subparagraph (A)\u2014 (i) the nature and extent of the commercial activity related to the good, ware, article, or merchandise; (ii) the gross revenue and net profits, if any, attributable to the good, ware, article, or merchandise; (iii) the alternative sourcing options for the good, ware, article, or merchandise, while protecting proprietary information of the issuer and any other cited business; (iv) a description of the measures taken by the issuer to exercise due diligence on the source and chain of custody of the good, ware, article, or merchandise; and (v) other entities and facilities affiliated with the facility employing forced labor, including the physical location of such facilities and of the supplier entity\u2019s headquarters; and (D) the issuer or any affiliate of the issuer, directly or indirectly, was involved in the development or provision of surveillance goods, services, or technologies (including telecommunications, information security, and sensors) used to facilitate gross human rights abuses. (2) Availability of information The Commission shall make all information disclosed pursuant to this subsection available to the public on the website of the Commission. (3) Definitions In this subsection, the terms forced labor and XUAR have the meaning given those terms, respectively, under section 12(m)(8). .\n##### (b) Repeal\nThe amendment made by this section shall be repealed on the earlier of\u2014\n**(1)**\nthe date that is 8 years after the date of the enactment of this section; or\n**(2)**\nthe date on which the President submits to Congress (including the Office of the Law Revision Council) a determination that the Government of the People\u2019s Republic of China has ended mass internment, forced labor, and any other gross violations of human rights experienced by Uyghurs, Kazakhs, Kyrgyz, and members of other persecuted groups in the Xinjiang Uyghur Autonomous Region.\n#### 4. Reports\n##### (a) Securities and Exchange Commission annual report to Congress\nThe Securities and Exchange Commission shall\u2014\n**(1)**\nconduct an annual assessment of the compliance of issuers with the requirements of section 12(m) of the Securities Exchange Act of 1934 on\u2014\n**(A)**\nissuers described under paragraph (1)(A) of such section 12(m);\n**(B)**\nissuers described under paragraph (1)(B) of such section 12(m); and\n**(C)**\nissuers described under paragraph (1)(C) of such section 12(m);\n**(2)**\nconduct an annual assessment of the compliance of issuers with the requirements of section 13(t) of the Securities Exchange Act of 1934; and\n**(3)**\nissue a report to Congress containing the results of the assessments under paragraph (1) and (2).\n##### (b) GAO report\nThe Comptroller General of the United States shall periodically evaluate and report to Congress on the effectiveness of the oversight by the Commission of the certification requirements under section 12(m) and section 13(t) of the Securities Exchange Act of 1934.",
      "versionDate": "2026-05-07",
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
        "updateDate": "2026-05-21T18:33:49Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8712ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Uyghur Forced Labor Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T07:38:33Z"
    },
    {
      "title": "Uyghur Forced Labor Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T07:38:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to require issuers to make certain disclosures relating to the Xinjiang Uyghur Autonomous Region, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T07:33:44Z"
    }
  ]
}
```
