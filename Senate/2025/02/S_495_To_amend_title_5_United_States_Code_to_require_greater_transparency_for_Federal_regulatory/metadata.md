# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/495?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/495
- Title: Prove It Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 495
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-05-08T17:37:08Z
- Update date including text: 2026-05-08T17:37:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-11-19 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-11-19 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/495",
    "number": "495",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Prove It Act of 2025",
    "type": "S",
    "updateDate": "2026-05-08T17:37:08Z",
    "updateDateIncludingText": "2026-05-08T17:37:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-10",
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
        "item": {
          "date": "2025-11-19T20:16:52Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-10T21:31:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s495is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 495\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to require greater transparency for Federal regulatory decisions that impact small businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prove It Act of 2025 .\n#### 2. Initial regulatory flexibility analysis\n##### (a) In general\nChapter 6 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 603(b)\u2014\n**(A)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(B)**\nby adding at the end the following:\n(6) where feasible, any reasonably foreseeable potential indirect costs the proposed rule may impose on small entities, including small entities that\u2014 (A) purchase products or services from, sell products or services to, or otherwise conduct business with entities directly regulated by the rule; (B) are directly regulated by other governmental entities as a result of the rule; or (C) are not directly regulated by the agency as a result of the rule but are otherwise subject to other agency rules as a result of the rule. ;\n**(2)**\nin section 605(b), by striking The agency and inserting Not later than 10 days after completing the certification described in this subsection, the agency ; and\n**(3)**\nby inserting after section 605 the following:\n605A. Review procedures relating to initial regulatory flexibility analysis certifications (a) Filing a petition To review agency certification of a proposed rule (1) In general Any small entity, group of small entities, or organization representing the interests of small entities may petition the Chief Counsel for Advocacy of the Small Business Administration (in this section referred to as the Chief Counsel ) to review a certification published under section 605(b) that a proposed rule will not, if promulgated, have a significant economic impact on a substantial number of small entities. (2) Form The Chief Counsel shall\u2014 (A) determine the method, timing, and form of disseminating a petition described in paragraph (1); and (B) display the information described in subparagraph (A) on the website of the Office of Advocacy of the Small Business Administration in a conspicuous manner. (3) Contents Each petition described in paragraph (1) with respect to a certification published under section 605(b) for a proposed rule shall clearly and concisely\u2014 (A) specify the name of the petitioner and a telephone number, a mailing address, and an email address that the Chief Counsel may use to communicate with the petitioner; (B) if the petitioner is an organization, provide additional identifying information, as applicable, including the organizational or corporate status of the petitioner, the State of incorporation of the petitioner, the registered agent of the petitioner, the interest of the petitioner in representing small entities affected by the proposed rule and the certification at issue, and the name and authority of the individual who signed the petition on behalf of the organizational or corporate petitioner; (C) present the specific problems or issues that the petitioner believes should be addressed or considered through a review of the certification, such as\u2014 (i) any specific circumstances in which the determination of the certification that the proposed rule will not, if promulgated, have a significant economic impact on a substantial number of small entities is incorrect, incomplete, or inadequate; or (ii) why the proposed rule would, if promulgated, have a significant economic impact on a substantial number of small entities; (D) cite, enclose, or reference any relevant and non-protected or confidential technical, scientific, or other data or information supporting any assertion of the problems or issues with the certification; (E) present a proposed solution to the problems or issues raised in the petition, including potential regulatory or compliance alternatives to the proposed rule; (F) provide an analysis, discussion, or argument that explains how the proposed solution described in subparagraph (E) solves the problems or issues raised in the petition; and (G) cite, enclose, or reference any other publicly available data or information supporting the proposed solution described in subparagraph (E). (b) Consultation (1) In general Any entity or organization desiring to file a petition under subsection (a) may request a consultation with the Chief Counsel before or after filing the petition. (2) Form The Chief Counsel shall\u2014 (A) determine the method, timing, and form of requesting a consultation with the Chief Counsel under paragraph (1); and (B) display the information described in subparagraph (A) on the website of the Office of Advocacy of the Small Business Administration in a conspicuous manner. (3) Limitations on assistance In any consultation regarding a petition under paragraph (1), the Chief Counsel\u2014 (A) may only\u2014 (i) describe the process for filing, docketing, tracking, closing, amending, withdrawing, and resolving the petition; and (ii) assist the petitioner to clarify the petition so that the Chief Counsel is able to understand the issues of concern to the petitioner; and (B) may not advise a petitioner on whether the petition should be amended or withdrawn. (c) Prima facie review (1) In general Upon receipt of a petition filed under this section with respect to the certification of a proposed rule, the Chief Counsel shall make an initial prima facie determination on the merit of the issues raised in the petition as to the properness of the certification and whether the proposed rule in question would, if promulgated, have a significant economic impact on a substantial number of small entities. (2) No further review If, following the prima facie review of a petition under paragraph (1), the Chief Counsel determines that the issues raised in the petition do not merit further review by the Chief Counsel, the Chief Counsel shall, not later than 10 days after receipt of the petition, inform the petitioner of that determination and the matter shall be closed. (3) Further review If, following the prima facie review of a petition under paragraph (1), the Chief Counsel determines that the issues raised in the petition do merit further review by the Chief Counsel, the Chief Counsel shall, not later than 10 days after receipt of the petition, inform the petitioner and the agency that promulgated the proposed rule that the Chief Counsel shall conduct a full review of the certification and proposed rule to which the petition relates under subsection (d). (d) Full review (1) Considerations; meeting In conducting a full review under this subsection with respect to the certification made under section 605(b), the Chief Counsel shall\u2014 (A) consider\u2014 (i) whether the agency that promulgated the proposed rule correctly determined which small entities will be affected by the proposed rule; (ii) whether the agency considered adequate economic data to assess whether the proposed rule will have a significant impact on a substantial number of small entities; and (iii) the economic implications of the proposed rule; and (B) convene a virtual or in-person meeting between the Chief Counsel, the petitioner, representatives of the agency that promulgated the proposed rule who are determined appropriate by the Chief Counsel, and the Administrator of the Office of Information and Regulatory Affairs to\u2014 (i) provide positions and support for those positions regarding the certification of the proposed rule; and (ii) allow the Chief Counsel to ask questions as the Chief Counsel determines necessary to make a final determination as to the validity of the certification. (2) Publication Not later than 30 days after the date on which the Chief Counsel begins a full review of a certification made with respect to a proposed rule under paragraph (1), the Chief Counsel shall submit to the petitioner and the agency that promulgated the proposed rule, and publish in the Federal Register and on the website of the Office of Advocacy of the Small Business Administration, the results of the review conducted under paragraph (1). (3) Requirement to perform analyses If, after a full review of a certification made with respect to a proposed rule under paragraph (1), the Chief Counsel determines that the proposed rule will, if promulgated, have a significant economic impact on a substantial number of small entities, the agency that promulgated the proposed rule shall perform an initial regulatory flexibility analysis and a final regulatory flexibility analysis for the proposed rule under sections 603 and 604, respectively. (4) Penalty If an agency fails to attend the required meeting under paragraph (1)(B) or in any other way fails to assist the Chief Counsel in a full review under paragraph (1) with respect to a proposed rule of the agency, as determined by the Chief Counsel, the final rule shall not apply to small entities. (5) Judicial review For purposes of judicial review under chapter 7 of this title, a certification made by an agency under section 605(b) for which a petition is filed under subsection (a) shall be considered final agency action as of the date on which the Chief Counsel\u2014 (A) makes a determination under subsection (c)(2) that the issues raised in the petition do not merit further review; or (B) publishes the results of a full review of the certification under paragraph (1). .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 6 of title 5, United States Code, is amended by inserting after the item relating to section 605 the following:\n605A. Review procedures relating to initial regulatory flexibility analysis certifications. .\n#### 3. Publication of guidance\nSection 609 of title 5, United States Code, is amended by adding at the end the following:\n(f) With respect to any rule that an agency determines is likely to have a significant economic impact on a substantial number of small entities, the head of the agency shall, on regulations.gov or any similar internet website\u2014 (1) publish all guidance documents and other relevant documents, as determined by the agency, including any updated guidance documents that set forth interpretations of the rule; and (2) allow for comments on the documents described in paragraph (1) to ensure that small entities may access and provide feedback on those documents. .\n#### 4. Review procedures for section 610 periodic review of rules\n##### (a) In general\nSection 610 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking the following factors ;\n**(B)**\nin paragraph (4), by striking and at the end;\n**(C)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(6) any indirect costs described in the initial regulatory flexibility analysis under section 603(b)(6), and any other indirect costs that may have arisen during the 10-year period described in subsection (a). ; and\n**(2)**\nby adding at the end the following:\n(d) If an agency fails to conduct a review of a rule as required under this section within the 10-year period described in subsection (a)\u2014 (1) the Chief Counsel for Advocacy of the Small Business Administration shall notify the agency that the rule has ceased to be effective; (2) the agency shall publish in the Federal Register a notification that the rule has ceased to be effective, and solicit comments for why the rule should be reinstated; and (3) if, based on the comments received under paragraph (2), the agency determines that the rule should be reinstated\u2014 (A) the agency shall have 180 days beginning on the date of that determination to complete the review of the rule under this section; and (B) upon completion of the review under subparagraph (A), the rule shall be reinstated, notwithstanding the notice and comment rulemaking procedures under section 553 of this title. .\n##### (b) Application\nThe amendment made by subsection (a)(2) shall apply with respect to any final rule issued by an agency\u2014\n**(1)**\nduring the 5-year period preceding the date of enactment of this Act; or\n**(2)**\non or after the date of enactment of this Act.\n#### 5. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act or the amendments made by this Act.",
      "versionDate": "2025-02-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-05-04",
        "text": "Placed on the Union Calendar, Calendar No. 552."
      },
      "number": "1163",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prove It Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-12T18:37:05Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-05-12T18:37:05Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-12T18:37:05Z"
          },
          {
            "name": "Small Business Administration",
            "updateDate": "2025-05-12T18:37:05Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-05-12T18:37:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T13:19:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s495",
          "measure-number": "495",
          "measure-type": "s",
          "orig-publish-date": "2025-02-10",
          "originChamber": "SENATE",
          "update-date": "2026-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s495v00",
            "update-date": "2026-05-08"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prove It Act of 2025</strong></p><p>This bill expands the requirements for federal agency rulemaking with respect to small businesses, organizations, and governmental jurisdictions.</p><p>Specifically, when conducting an initial regulatory flexibility analysis, agencies must include, where feasible, any reasonably foreseeable potential indirect costs the proposed rule may impose on such small entities.</p><p>Further, if an agency certifies that an initial regulatory flexibility analysis is not required because the rule will not have a significant economic impact on a substantial number of small entities, the agency must provide such certification within 10 days to the Office of Advocacy of the Small Business Administration. A small entity or group of small entities may petition the Office of Advocacy to review such certification. The petition must include specified information, such as the issues the petitioner believes should be addressed and a proposed solution to the issues raised.</p><p>If the Office of Advocacy ultimately determines, upon a full review of the petition, that the proposed rule would have a significant economic impact on a\u00a0substantial number of small entities, the agency promulgating the rule must perform an initial\u00a0and final regulatory flexibility analysis for the rule. Additionally, if the agency does not participate or assist in the full review process, the finalized rule shall not apply to small entities.</p><p>The bill also requires agencies to publish, and allow for comments on, all guidance documents with respect to any rule an agency determines is likely to have a significant economic impact on a substantial number of small entities.</p>"
        },
        "title": "Prove It Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s495.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prove It Act of 2025</strong></p><p>This bill expands the requirements for federal agency rulemaking with respect to small businesses, organizations, and governmental jurisdictions.</p><p>Specifically, when conducting an initial regulatory flexibility analysis, agencies must include, where feasible, any reasonably foreseeable potential indirect costs the proposed rule may impose on such small entities.</p><p>Further, if an agency certifies that an initial regulatory flexibility analysis is not required because the rule will not have a significant economic impact on a substantial number of small entities, the agency must provide such certification within 10 days to the Office of Advocacy of the Small Business Administration. A small entity or group of small entities may petition the Office of Advocacy to review such certification. The petition must include specified information, such as the issues the petitioner believes should be addressed and a proposed solution to the issues raised.</p><p>If the Office of Advocacy ultimately determines, upon a full review of the petition, that the proposed rule would have a significant economic impact on a\u00a0substantial number of small entities, the agency promulgating the rule must perform an initial\u00a0and final regulatory flexibility analysis for the rule. Additionally, if the agency does not participate or assist in the full review process, the finalized rule shall not apply to small entities.</p><p>The bill also requires agencies to publish, and allow for comments on, all guidance documents with respect to any rule an agency determines is likely to have a significant economic impact on a substantial number of small entities.</p>",
      "updateDate": "2026-05-08",
      "versionCode": "id119s495"
    },
    "title": "Prove It Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prove It Act of 2025</strong></p><p>This bill expands the requirements for federal agency rulemaking with respect to small businesses, organizations, and governmental jurisdictions.</p><p>Specifically, when conducting an initial regulatory flexibility analysis, agencies must include, where feasible, any reasonably foreseeable potential indirect costs the proposed rule may impose on such small entities.</p><p>Further, if an agency certifies that an initial regulatory flexibility analysis is not required because the rule will not have a significant economic impact on a substantial number of small entities, the agency must provide such certification within 10 days to the Office of Advocacy of the Small Business Administration. A small entity or group of small entities may petition the Office of Advocacy to review such certification. The petition must include specified information, such as the issues the petitioner believes should be addressed and a proposed solution to the issues raised.</p><p>If the Office of Advocacy ultimately determines, upon a full review of the petition, that the proposed rule would have a significant economic impact on a\u00a0substantial number of small entities, the agency promulgating the rule must perform an initial\u00a0and final regulatory flexibility analysis for the rule. Additionally, if the agency does not participate or assist in the full review process, the finalized rule shall not apply to small entities.</p><p>The bill also requires agencies to publish, and allow for comments on, all guidance documents with respect to any rule an agency determines is likely to have a significant economic impact on a substantial number of small entities.</p>",
      "updateDate": "2026-05-08",
      "versionCode": "id119s495"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s495is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Prove It Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prove It Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to require greater transparency for Federal regulatory decisions that impact small businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:46Z"
    }
  ]
}
```
