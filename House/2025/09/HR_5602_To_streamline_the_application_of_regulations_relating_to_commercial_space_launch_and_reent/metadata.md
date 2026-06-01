# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5602
- Title: LAUNCH Act
- Congress: 119
- Bill type: HR
- Bill number: 5602
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-04-20T20:50:43Z
- Update date including text: 2026-04-20T20:50:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5602",
    "number": "5602",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LAUNCH Act",
    "type": "HR",
    "updateDate": "2026-04-20T20:50:43Z",
    "updateDateIncludingText": "2026-04-20T20:50:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5602ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5602\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Pfluger (for himself and Mr. Whitesides ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo streamline the application of regulations relating to commercial space launch and reentry requirements and licensing of private remote sensing space systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Licensing Aerospace Units to New Commercial Heights Act or the LAUNCH Act .\n#### 2. Streamlining regulations relating to commercial space launch and reentry requirements\n##### (a) Evaluation of implementation of part 450\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Transportation (referred to in this Act as the Secretary ) shall evaluate the implementation of part 450 of title 14, Code of Federal Regulations (in this section referred to as part 450 ) and the impacts of part 450 on the commercial spaceflight industry.\n**(2) Elements**\nThe evaluation required by paragraph (1) shall include an assessment of\u2014\n**(A)**\nwhether increased uncertainty in the commercial spaceflight industry has resulted from the implementation of part 450;\n**(B)**\nwhether part 450 has resulted in operational delays to launch; and\n**(C)**\nwhether timelines for reviews have changed, including an assessment of the impact of the incremental review process on those timelines and the root cause for multiple reviews, if applicable.\n**(3) Report required**\nNot later than 90 days after completing the review required by paragraph (1), the Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that includes\u2014\n**(A)**\nthe findings of the review;\n**(B)**\nrecommendations for reducing delays and inefficiencies resulting from part 450 that do not rely solely on additional personnel or funding; and\n**(C)**\nan estimate for a timeline and funding for implementing the recommendations described in subparagraph (B).\n##### (b) Rulemaking committee\n**(1) In general**\nThe Secretary shall continue to support an Aerospace Rulemaking Committee for the commercial space transportation industry, comprised of established and emerging United States commercial space launch and reentry services providers (including providers that hold, and providers that have applied for but not yet received, licenses issued under chapter 509 of title 51, United States Code)\u2014\n**(A)**\nto facilitate industry participation in developing recommendations for amendments to part 450 to address the challenges identified in conducting the review required by subsection (a) or under paragraph (2) of section 50905(d) of title 51, United States Code (as added by subsection (d)(3)); and\n**(B)**\nto provide a long-term forum for the United States commercial spaceflight industry to share perspectives relating to regulations affecting the industry.\n**(2) Prevention of duplicative efforts**\nThe Secretary shall ensure that an Aerospace Rulemaking Committee established under this subsection does not provide services or make efforts that are duplicative of the services provided and efforts made by the Commercial Space Transportation Advisory Committee.\n##### (c) Encouragement of innovation\nThe Secretary shall, on an ongoing basis, determine whether any requirements for a license issued under chapter 509 of title 51, United States Code, can be modified or eliminated to encourage innovative new technologies and operations.\n##### (d) Modifications to requirements and procedures for license applications\n**(1) Consideration of safety rationales of license applicants**\nSection 50905(a)(2) of title 51, United States Code, is amended\u2014\n**(A)**\nby striking Secretary may inserting the following: \u201cSecretary\u2014\n(A) may ;\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(B) shall accept a reasonable safety rationale proposed by an applicant for a license under this chapter, including new approaches, consistent with paragraph (1). .\n**(2) Facilitation of license applications and assistance to applicants**\nSection 50905(a) of title 51, United States Code, is amended by adding at the end the following:\n(3) In carrying out paragraph (1), the Secretary shall assign a licensing team lead to each applicant for a license under this chapter to assist the applicant in streamlining the process for reviewing and approving the license application. .\n**(3) Streamlining of review processes**\nSection 50905(d) of title 51, United States Code, is amended by striking the end period and inserting the following: \u201c, including by\u2014\n(1) adjudicating determinations with respect to such applications and revisions to such determinations in a timely manner as part of the incremental review process under section 450.33 of title 14, Code of Federal Regulations (or a successor regulation); and (2) eliminating and streamlining duplicative review processes with other agencies, particularly relating to the use of Federal ranges or requirements to use the assets of Federal ranges. .\n#### 3. Digital licensing, permitting, and approval system\n##### (a) In general\nSection 50905 of title 51, United States Code, is amended by adding at the end the following:\n(e) Digital licensing, permitting, and approval system (1) Establishment (A) In general Subject to paragraph (4), not later than 60 days after the date of the enactment of this subsection, the Secretary shall develop and maintain a digital licensing, permitting, and approval system\u2014 (i) to accept, track, and provide relevant status information regarding each license or permit application under this chapter, beginning with receipt of the initial application through final approval or denial of the application; and (ii) to provide notifications to an applicant with respect to the status of such an application. (B) Elements The system required by subparagraph (A) shall include, at a minimum, information on\u2014 (i) the date on which an application was received by the Secretary; (ii) each date on which the application was referred to any other agency of the Federal Government for review, as applicable; (iii) each date on which additional information was requested from the applicant, as applicable; (iv) the date on which the Secretary notified the applicant of a final approval or denial of the application; and (v) the overall rate of success of such system in meeting the timelines set forth in this section. (2) Public availability The Secretary shall\u2014 (A) make the information maintained by the system required by paragraph (1) available on a publicly accessible website of the Department of Transportation; and (B) ensure that such information is updated on such website not less frequently than quarterly. (3) Notification With respect to an application for a license or permit under this chapter, the Secretary shall provide through the digital licensing, permitting, and approval system developed under this subsection electronic notification to an applicant\u2014 (A) immediately on\u2014 (i) receipt of a license or permit application; (ii) a determination under subsection (f) that an application received by the Secretary is complete; (iii) initiation of application processing; (iv) transmission of the application, in whole or part, for interagency review, as applicable, and such notification shall include an identification of the 1 or more agencies with which application information is shared; and (v) approval or denial of the application; and (B) with respect to\u2014 (i) any question proposed by the Secretary to the applicant; (ii) responses provided to the Secretary by any agency involved in interagency review, as applicable; and (iii) any other status update the Secretary considers necessary. (4) Existing systems In carrying out paragraph (1), the Secretary shall utilize a commercially available system that can be used off-the-shelf. (f) Complete application An application submitted under this section shall be considered complete if, at the time of electronic submission, the applicant has provided in standard digital format all information required under subsection (b). .\n##### (b) Funding\nOf the amounts made available for the Federal Aviation Administration for Commercial Space Transportation Safety Research and Development for fiscal year 2025, not more than $5,000,000 may be made available to develop the digital licensing, permitting, and approval system described in section 50905(e) of title 51, United States Code.\n#### 4. Annual briefing on government processing of commercial space launch and reentry licenses\n##### (a) Requirement\nNot later than March 31 each calendar year, the Secretary shall brief the appropriate committees of Congress on the licensing and permitting process for space activities required by section 50905 of title 51, United States Code.\n##### (b) Elements\nThe briefing required by subsection (a) shall include, with respect to the preceding calendar year, the following:\n**(1)**\nThe average number of days that elapsed between the date on which an application is submitted and the date on which an applicant receives final approval or denial of the application.\n**(2)**\nThe frequency and average duration of tolling against submitted applications.\n**(3)**\nThe number of applications reviewed that exceeded the statutorily provided review timelines.\n**(4)**\nA description of efforts made by the Secretary to streamline, under section 50905(d) of title 51, United States Code, the processes required for review of applications.\n**(5)**\nA summary of the information generated by the digital licensing, permitting, and approval system established under section 50905(e) of title 51, United States Code, including any additional information the Secretary considers relevant with respect to the function or processes of such system.\n**(6)**\nAn assessment as to whether the application review process operates in a manner that encourages the global competitiveness of the commercial space industry of the United States.\n##### (c) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Commerce, Science, and Transportation and the Committee on Appropriations of the Senate; and\n**(2)**\nthe Committee on Science, Space, and Technology, the Committee on Transportation and Infrastructure, and the Committee on Appropriations of the House of Representatives.\n#### 5. Direct hire for Office of Commercial Space Transportation\n##### (a) In general\nThe Secretary of Transportation shall use direct hire authorities (as such authorities existed on the day before the date of the enactment of this Act) to hire individuals on a noncompetitive basis for positions related to space launch and reentry licensing and permit activities.\n##### (b) Annual report\nNot less frequently than annually, the Secretary of Transportation shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives an annual report on the use of direct hiring authorities to fill such positions within the Commercial Space Transportation Administration related to commercial space launch and reentry licensing and permit activities.\n#### 6. Establishment of Commercial Space Transportation Administration\n##### (a) In general\nChapter 509 of title 51, United States Code, is amended by inserting after section 50902 the following:\n50902A. Commercial Space Transportation Administration (a) Establishment There is established within the Department of Transportation a Commercial Space Transportation Administration. (b) Leadership The Commercial Space Transportation Administration shall be headed by an Administrator, who shall report directly to the Secretary of Transportation. (c) Duties The Administrator of the Commercial Space Transportation Administration shall exercise the authorities of the Secretary of Transportation with respect to commercial space launch and reentry activities, including the authorities provided under this chapter. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 509 of such title is amended by inserting after the item relating to section 50902 the following:\n50902A. Commercial Space Transportation Administration. .\n#### 7. Flight safety analysis workforce\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nflight safety analysis is critical to maintaining a high level of public safety for commercial space launches from, and reentries to, Federal ranges;\n**(2)**\nsignificant expertise in flight safety analysis exists within the Department of Defense, the Department of Transportation, and the National Aeronautics and Space Administration; and\n**(3)**\nthe increasing pace of commercial launch and reentries requires greater cooperation among the Secretary of Defense, the Secretary, and the Administrator of the National Aeronautics and Space Administration to support commercial launch and reentry activities at Federal ranges.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary, in consultation with the Secretary of Defense and the Administrator of the National Aeronautics and Space Administration, shall submit to the Committee on Commerce, Science, and Transportation and the Committee on Armed Services of the Senate and the Committee on Science, Space, and Technology and the Committee on Armed Services of the House of Representatives a report that identifies roles, responsibilities, expertise, and knowledge that exists within the executive branch of the Federal Government relating to analysis of flight safety for space launch and reentry activities.\n##### (c) Memorandum of understanding\nUpon completion of the report required by subsection (b), the Secretary may enter into a memorandum of understanding with the Secretary of Defense and the Administrator of the National Aeronautics and Space Administration to allow Federal range personnel to support flight safety analysis required for the licensing of commercial space launch and reentry activities.\n#### 8. Streamlining licensing of private remote sensing space systems\n##### (a) Clarification of remote sensing regulatory authority over certain imaging systems\nSection 60121(a)(2) of title 51, United States Code, is amended by adding at the end the following: Instruments determined by the Secretary in writing to be used primarily for mission assurance or other technical purposes shall not be considered to be conducting remote sensing. Instruments used primarily for mission assurance or other technical purposes are instruments used to support the health of the launch vehicle or the operator\u2019s spacecraft or the safety of the operator\u2019s space operations, including instruments used to support on-board self-monitoring for technical assurance, flight reliability, spaceflight safety, navigation, attitude control, separation events, payload deployments, or instruments collecting self-images. .\n##### (b) Facilitation of license applications and assistance to applicants\n**(1) In general**\nSection 60121 of title 51, United States Code, is amended\u2014\n**(A)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively; and\n**(B)**\nby inserting after subsection (c) the following:\n(d) Assignment of dedicated licensing officer The Secretary shall assign a licensing officer to oversee the application of the applicant for a license under subsection (a). The licensing officer shall assist the applicant by facilitating the application process, minimizing license conditions, and expediting the review and approval of the application, to the extent authorized by law. .\n**(2) Conforming amendment**\nSection 60122(b)(3) of title 51, United States Code, is amended by striking section 60121(e) and inserting section 60121(f) .\n##### (c) Transparency and expeditious review of licenses\nIn carrying out the authorities under subchapter III of chapter 601 of title 51, United States Code, the Secretary shall\u2014\n**(1)**\nprovide transparency to and engagement with applicants throughout the licensing process, including by stating with specificity to the applicant or licensee what basis caused the tiering determination of the license;\n**(2)**\nminimize the timelines for review of commercial remote sensing licensing applications; and\n**(3)**\nnot less frequently than annually, reevaluate the criteria for the tiering of satellite systems, with a goal of expeditiously recategorizing Tier 3 systems to a lower tier without temporary license conditions.\n#### 9. GAO report\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the policies, regulations, and practices of the Department of Commerce (referred to in this section as the Department ) with respect to the private remote sensing space industry.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn assessment of the extent to which such licensing policies, regulations, and practices of the Department promote or inhibit a robust domestic private remote sensing industry, including any restrictions that impede innovative remote sensing capabilities.\n**(2)**\nRecommendations on changes to policies, regulations, and practices for consideration by the Secretary of Commerce to promote United States industry leadership in private remote sensing capabilities, including recommendations for\u2014\n**(A)**\ndetermining whether the costs to industry outweigh the benefits of conducting on-site ground station visits, and possible alternatives to ensuring compliance;\n**(B)**\nassessing the information in a license application that should be treated as a material fact and the justification for such treatment;\n**(C)**\nincorporating industry feedback into Department policies, regulations, and practices; and\n**(D)**\nincreasing Department transparency by\u2014\n**(i)**\nensuring the wide dissemination of Department guidance;\n**(ii)**\nproviding clear application instructions; and\n**(iii)**\nestablishing written precedent of Department actions.",
      "versionDate": "2025-09-26",
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
        "actionDate": "2025-06-05",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1961",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LAUNCH Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-18T18:16:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-26",
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
          "measure-id": "id119hr5602",
          "measure-number": "5602",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-26",
          "originChamber": "HOUSE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5602v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-09-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Licensing Aerospace Units to New Commercial Heights Act or the LAUNCH Act</strong></p><p>This bill makes changes to, and requires certain evaluations of, regulatory processes for licensing commercial space launch and reentry activities and private remote sensing systems.</p><p>The Federal Aviation Administration (FAA) Office of Commercial Space Transportation regulates the launch and reentry of commercial spacecraft. In 2020, the FAA consolidated launch and reentry licensing requirements for all types of space vehicles into a single set of regulations, known as Part 450.</p><p>The bill requires the FAA to evaluate and report on the implementation of Part 450 and its impacts on the commercial spaceflight industry, including whether the rule has resulted in uncertainty or operational delays. The FAA must also continue an aerospace rulemaking committee comprised of launch and reentry service providers.</p><p>Further, the FAA must develop a digital system to accept commercial space launch and reentry applications and provide status information and notifications to applicants.</p><p>The bill elevates the Office of Commercial Space Transportation to a modal administration reporting directly to the Department of Transportation (DOT). The administration must exercise all of DOT\u2019s authorities related to commercial space launch and reentry.</p><p>Finally, the bill revises the licensing process for private remote sensing systems and requires the Government Accountability Office to report on the Department of Commerce\u2019s regulation of the private remote sensing industry. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p>"
        },
        "title": "LAUNCH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5602.xml",
    "summary": {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Licensing Aerospace Units to New Commercial Heights Act or the LAUNCH Act</strong></p><p>This bill makes changes to, and requires certain evaluations of, regulatory processes for licensing commercial space launch and reentry activities and private remote sensing systems.</p><p>The Federal Aviation Administration (FAA) Office of Commercial Space Transportation regulates the launch and reentry of commercial spacecraft. In 2020, the FAA consolidated launch and reentry licensing requirements for all types of space vehicles into a single set of regulations, known as Part 450.</p><p>The bill requires the FAA to evaluate and report on the implementation of Part 450 and its impacts on the commercial spaceflight industry, including whether the rule has resulted in uncertainty or operational delays. The FAA must also continue an aerospace rulemaking committee comprised of launch and reentry service providers.</p><p>Further, the FAA must develop a digital system to accept commercial space launch and reentry applications and provide status information and notifications to applicants.</p><p>The bill elevates the Office of Commercial Space Transportation to a modal administration reporting directly to the Department of Transportation (DOT). The administration must exercise all of DOT\u2019s authorities related to commercial space launch and reentry.</p><p>Finally, the bill revises the licensing process for private remote sensing systems and requires the Government Accountability Office to report on the Department of Commerce\u2019s regulation of the private remote sensing industry. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr5602"
    },
    "title": "LAUNCH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Licensing Aerospace Units to New Commercial Heights Act or the LAUNCH Act</strong></p><p>This bill makes changes to, and requires certain evaluations of, regulatory processes for licensing commercial space launch and reentry activities and private remote sensing systems.</p><p>The Federal Aviation Administration (FAA) Office of Commercial Space Transportation regulates the launch and reentry of commercial spacecraft. In 2020, the FAA consolidated launch and reentry licensing requirements for all types of space vehicles into a single set of regulations, known as Part 450.</p><p>The bill requires the FAA to evaluate and report on the implementation of Part 450 and its impacts on the commercial spaceflight industry, including whether the rule has resulted in uncertainty or operational delays. The FAA must also continue an aerospace rulemaking committee comprised of launch and reentry service providers.</p><p>Further, the FAA must develop a digital system to accept commercial space launch and reentry applications and provide status information and notifications to applicants.</p><p>The bill elevates the Office of Commercial Space Transportation to a modal administration reporting directly to the Department of Transportation (DOT). The administration must exercise all of DOT\u2019s authorities related to commercial space launch and reentry.</p><p>Finally, the bill revises the licensing process for private remote sensing systems and requires the Government Accountability Office to report on the Department of Commerce\u2019s regulation of the private remote sensing industry. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119hr5602"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5602ih.xml"
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
      "title": "LAUNCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T10:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LAUNCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Licensing Aerospace Units to New Commercial Heights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To streamline the application of regulations relating to commercial space launch and reentry requirements and licensing of private remote sensing space systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T10:03:14Z"
    }
  ]
}
```
