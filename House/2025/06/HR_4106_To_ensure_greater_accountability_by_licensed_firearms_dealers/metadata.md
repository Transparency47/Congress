# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4106
- Title: Prevent Illegal Gun Sales Act
- Congress: 119
- Bill type: HR
- Bill number: 4106
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-05-19T15:53:21Z
- Update date including text: 2026-05-19T15:53:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4106",
    "number": "4106",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Prevent Illegal Gun Sales Act",
    "type": "HR",
    "updateDate": "2026-05-19T15:53:21Z",
    "updateDateIncludingText": "2026-05-19T15:53:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "GA"
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
      "sponsorshipDate": "2025-06-24",
      "state": "DC"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MO"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4106ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4106\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Magaziner (for himself, Mr. Johnson of Georgia , Ms. Norton , Ms. DelBene , Ms. Schakowsky , Mr. Krishnamoorthi , and Ms. Kelly of Illinois ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo ensure greater accountability by licensed firearms dealers.\n#### 1. Short title\nThis Act may be cited as the Prevent Illegal Gun Sales Act .\n#### 2. Increasing the number of allowed compliance inspections of firearms dealers\nSection 923(g)(1)(B)(ii)(I) of title 18, United States Code, is amended by striking once and inserting 3 times .\n#### 3. Increasing penalties on firearms licensees\nSection 924(a)(3) of title 18, United States Code, is amended in the matter following subparagraph (B) by striking one year and inserting 5 years .\n#### 4. Serious recordkeeping offenses that aid gun trafficking\nSection 924(a)(3) of title 18, United States Code, is amended by striking the period at the end and inserting . If the conduct described in subparagraph (A) or (B) is in relation to an offense under subsection (a)(6) or (d) of section 922, the licensed dealer, licensed importer, licensed manufacturer, or licensed collector shall be fined under this title, imprisoned for not more than 10 years, or both. .\n#### 5. Suspension of firearms dealer\u2019s license and civil penalties for violations of the Gun Control Act\nSection 923 of title 18, United States Code, is amended by striking subsections (e) and (f) and inserting the following:\n(e) (1) (A) The Attorney General may, after notice and opportunity for hearing, suspend or revoke any license issued under this section, or may subject the licensee to a civil penalty of not more than $10,000 per violation, if the holder of the license\u2014 (i) has violated any provision of this chapter or any rule or regulation prescribed by the Attorney General under this chapter; or (ii) except as provided in subparagraph (B), fails to have secure gun storage or safety devices available at any place in which firearms are sold under the license to persons who are not licensees. (B) Subparagraph (A)(ii) shall not apply in any case in which a secure gun storage or safety device is temporarily unavailable because of theft, casualty loss, consumer sales, backorders from a manufacturer, or any other similar reason beyond the control of the licensee. (2) The Attorney General may, after notice and opportunity for hearing, suspend or revoke the license of, or assess a civil penalty of not more than $10,000 on, a dealer who transfers armor piercing ammunition. (3) The Attorney General may at any time compromise, mitigate, or remit the liability with respect to any violation of this chapter or any rule or regulation prescribed by the Attorney General under this chapter. (4) The Attorney General\u2019s actions under this subsection may be reviewed only as provided in subsection (f). (f) (1) Any person whose application for a license is denied and any holder of a license which is suspended or revoked or who is assessed a civil penalty shall receive a written notice from the Attorney General stating specifically the grounds upon which the application was denied or upon which the license was suspended or revoked or the civil penalty assessed. Any notice of a suspension or revocation of a license shall be given to the holder of the license before the effective date of the suspension or revocation. (2) If the Attorney General denies an application for a license, or suspends or revokes a license, or assesses a civil penalty, the Attorney General shall, upon request by the aggrieved party, promptly hold a hearing to review the denial, suspension, revocation, or assessment. In the case of a suspension or revocation of a license, the Attorney General shall, on the request of the holder of the license, stay the effective date of the suspension or revocation. A hearing under this paragraph shall be held at a location convenient to the aggrieved party. (3) (A) If after a hearing held under paragraph (2) the Attorney General decides not to reverse the decision to deny an application or suspend or revoke a license or assess a civil penalty, the Attorney General shall give notice of the decision to the aggrieved party. (B) The aggrieved party may at any time within 60 days after the date notice is given under subparagraph (A) file a petition with the United States district court for the district in which the party resides or in which the party\u2019s principal place of business is located for a de novo judicial review of the denial, suspension, revocation, or assessment. (C) In a proceeding conducted under this paragraph, the court may consider any evidence submitted by the parties to the proceeding without regard to whether such evidence was considered at the hearing held under paragraph (2). (D) If the court decides that the Attorney General was not authorized to deny the application or to suspend or revoke the license or to assess the civil penalty, the court shall order the Attorney General to take such action as may be necessary to comply with the judgment of the court. .\n#### 6. Termination of firearms dealer\u2019s license upon felony conviction\nSection 925(b) of title 18, United States Code, is amended by striking until any conviction pursuant to the indictment becomes final and inserting until the date of any conviction pursuant to the indictment .\n#### 7. Authority to hire additional personnel\nThe Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives may hire at least 80 additional employees for the purpose of carrying out additional inspections as provided for in the amendments made by this Act.\n#### 8. Authority to require licensed dealer to conduct a physical inventory and provide inventory record if dealer has unlawfully transferred a firearm or 10 or more crime guns are traced to the dealer\n##### (a) In general\nSection 923(g)(1) of title 18, United States Code, is amended by adding at the end the following:\n(E) The Attorney General may require a licensed importer, licensed manufacturer, or licensed dealer to conduct a physical inventory of the firearms in the business inventory of the licensee, and provide the Attorney General with a detailed record of the physical inventory if\u2014 (i) the licensee has been convicted of transferring a firearm unlawfully; or (ii) the Attorney General finds that 10 or more firearms used in a crime under Federal, State, or local law have been traced back to the licensee. .\n##### (b) Conforming amendments\n**(1)**\nSection 923(j) of such title is amended in the 6th sentence by inserting , except as required under subsection (g)(1)(E) before the period.\n**(2)**\nThe matter under the heading salaries and expenses under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives under title II of division B of the Consolidated and Further Continuing Appropriations Act, 2013 ( Public Law 113\u20136 ; 127 Stat. 247) is amended in the 5th proviso by inserting , except as required under subsection (g)(1)(E) of such section 923 before the colon.\n#### 9. Issuance of licenses\nSection 923 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby inserting (1) before Upon ;\n**(B)**\nin the first sentence, by inserting , subject to paragraph (2), after Attorney General shall ; and\n**(C)**\nby adding at the end the following:\n(2) The Attorney General may deny an application submitted under subsection (a) or (b) if the Attorney General determines that\u2014 (A) issuing the license would pose a danger to public safety; or (B) the applicant\u2014 (i) is not likely to comply with the law; or (ii) is otherwise not suitable to be issued a license. ; and\n**(2)**\nin subsection (d)(1), in the matter preceding subparagraph (A), by inserting , subject to subsection (c)(2), after shall .\n#### 10. Liability standards\nSection 923 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c), in the third sentence, by striking willfully ; and\n**(2)**\nin subsection (d), by striking willfully each place it appears.\n#### 11. Regulatory flexibility\nSection 926(a) of title 18, United States Code, is amended, in the matter preceding paragraph (1), by striking only .\n#### 12. Report to Congress\nThe Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives shall submit biennial reports to Congress on the implementation of this Act and the amendments made by this Act, which shall include\u2014\n**(1)**\na statement by the Director as to what additional resources, if any, are necessary in order to implement this Act and the amendments made by this Act; and\n**(2)**\nany recommendations of the Director for how better to ensure that\u2014\n**(A)**\nfirearms dealers are complying with all laws and regulations that apply with respect to dealing in firearms; and\n**(B)**\nnoncompliant firearms dealers are subject to appropriate action in a timely manner.\n#### 13. Severability\nIf any provision of this Act or of an amendment made by this Act, or the application of such a provision to any person or circumstance, is held to be invalid, the remainder of this Act or of such an amendment, or the application of this Act or of such an amendment to other persons or circumstances, shall not be affected.",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-06-24",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keeping Gun Dealers Honest Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-14T16:03:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-24",
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
          "measure-id": "id119hr4106",
          "measure-number": "4106",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-24",
          "originChamber": "HOUSE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4106v00",
            "update-date": "2026-05-19"
          },
          "action-date": "2025-06-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prevent Illegal Gun Sales Act</strong></p><p>This bill broadens the authority of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) to administer federal laws governing the licensing, inspection, and\u00a0enforcement of federally licensed dealers, importers, and manufacturers of firearms (federal firearms licensees, or FFLs). The bill also increases criminal penalties for FFLs and licensed collectors who commit certain recordkeeping violations.</p><p>With respect to licensing, the bill allows the ATF to deny an application for a federal firearms license if it would endanger public safety or if the applicant is unlikely to comply with the law.</p><p>Additionally, the bill enhances the ATF's inspection authority, including by increasing the maximum number of annual compliance inspections to three (currently, one) and by\u00a0authorizing an additional 80 personnel to conduct inspections.</p><p>The bill also expands the ATF's enforcement authority, including by allowing it to suspend the license of or impose a civil penalty on an FFL who violates federal firearms laws or regulations and by allowing it to require an FFL to conduct physical inventories if the FFL unlawfully transfers a firearm or if 10 or more firearms\u00a0used in a crime are traced back to the FFL.</p><p>Finally, the bill increases the maximum prison term to five years (currently, one year) for an FFL or licensed collector who knowingly makes a false statement or representation in required firearms records.</p>"
        },
        "title": "Prevent Illegal Gun Sales Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4106.xml",
    "summary": {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prevent Illegal Gun Sales Act</strong></p><p>This bill broadens the authority of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) to administer federal laws governing the licensing, inspection, and\u00a0enforcement of federally licensed dealers, importers, and manufacturers of firearms (federal firearms licensees, or FFLs). The bill also increases criminal penalties for FFLs and licensed collectors who commit certain recordkeeping violations.</p><p>With respect to licensing, the bill allows the ATF to deny an application for a federal firearms license if it would endanger public safety or if the applicant is unlikely to comply with the law.</p><p>Additionally, the bill enhances the ATF's inspection authority, including by increasing the maximum number of annual compliance inspections to three (currently, one) and by\u00a0authorizing an additional 80 personnel to conduct inspections.</p><p>The bill also expands the ATF's enforcement authority, including by allowing it to suspend the license of or impose a civil penalty on an FFL who violates federal firearms laws or regulations and by allowing it to require an FFL to conduct physical inventories if the FFL unlawfully transfers a firearm or if 10 or more firearms\u00a0used in a crime are traced back to the FFL.</p><p>Finally, the bill increases the maximum prison term to five years (currently, one year) for an FFL or licensed collector who knowingly makes a false statement or representation in required firearms records.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr4106"
    },
    "title": "Prevent Illegal Gun Sales Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prevent Illegal Gun Sales Act</strong></p><p>This bill broadens the authority of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) to administer federal laws governing the licensing, inspection, and\u00a0enforcement of federally licensed dealers, importers, and manufacturers of firearms (federal firearms licensees, or FFLs). The bill also increases criminal penalties for FFLs and licensed collectors who commit certain recordkeeping violations.</p><p>With respect to licensing, the bill allows the ATF to deny an application for a federal firearms license if it would endanger public safety or if the applicant is unlikely to comply with the law.</p><p>Additionally, the bill enhances the ATF's inspection authority, including by increasing the maximum number of annual compliance inspections to three (currently, one) and by\u00a0authorizing an additional 80 personnel to conduct inspections.</p><p>The bill also expands the ATF's enforcement authority, including by allowing it to suspend the license of or impose a civil penalty on an FFL who violates federal firearms laws or regulations and by allowing it to require an FFL to conduct physical inventories if the FFL unlawfully transfers a firearm or if 10 or more firearms\u00a0used in a crime are traced back to the FFL.</p><p>Finally, the bill increases the maximum prison term to five years (currently, one year) for an FFL or licensed collector who knowingly makes a false statement or representation in required firearms records.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr4106"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4106ih.xml"
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
      "title": "Prevent Illegal Gun Sales Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prevent Illegal Gun Sales Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure greater accountability by licensed firearms dealers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:28Z"
    }
  ]
}
```
