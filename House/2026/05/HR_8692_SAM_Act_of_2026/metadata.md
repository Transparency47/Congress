# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8692?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8692
- Title: SAM Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8692
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-22T10:23:36Z
- Update date including text: 2026-05-22T10:23:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8692",
    "number": "8692",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [I-CA-3]",
        "lastName": "Kiley",
        "party": "I",
        "state": "CA"
      }
    ],
    "title": "SAM Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T10:23:36Z",
    "updateDateIncludingText": "2026-05-22T10:23:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
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
          "date": "2026-05-07T13:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8692ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8692\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to allow certain grant funds issued by the Secretary of Transportation to be used for the deployment and purchasing of technology for certain autonomous shared mobility vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shared Autonomous Mobility Act of 2026 or SAM Act of 2026 .\n#### 2. Accelerating innovative mobility grant program\n##### (a) Amendment to chapter 53 defined terms\nSection 5302 of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (14)(B) by striking configuration or components and inserting configuration or components (including a major change to equip or facilitate automated driving systems) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(26) Covered shared mobility vehicle The term covered shared mobility vehicle means a new bus model equipped with an automated driving system. (27) Automated driving system With respect to a new bus model, the term automated driving system means a system of hardware and software that\u2014 (A) is collectively capable of performing the entire dynamic driving task on a sustained basis, regardless of whether such system is limited to a specific operational design domain; and (B) is a level 3, 4, or 5 vehicle driving automation system, as defined in the standard titled J3016_202104\u2014Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles and published by SAE International on April 29, 2021, or any substantially similar successor standard of SAE International. .\n##### (b) Program\nChapter 53 of title 49, United States Code, is amended by adding at the end the following new section:\n5341. Accelerating innovative mobility grant program (a) In general Not later than 90 days after the date of enactment of the Shared Autonomous Mobility Act of 2026 , the Secretary shall establish a program (referred to in this section as the Program ) under which the Secretary may make competitive grants to covered entities for use carrying out a project to accelerate the deployment of a covered shared mobility vehicle in accordance with this section. (b) Application (1) In general To be eligible to receive a grant under the Program, a covered entity shall submit to the Secretary an application\u2014 (A) during a 60-day submission period to be specified by the Secretary and occurring not less frequently than once annually; and (B) in such form and containing such information as the Secretary may require. (2) Solicitation The Secretary may solicit a covered entity to submit an application under paragraph (1). (c) Selection Not later than 60 days after the end of a submission period under subsection (b)(1)(A), the Secretary shall select for receipt of a Program grant such applicants as the Secretary determines appropriate based on criteria established by the Secretary. (d) Reservation of funds From the amounts made available under subsection (h) for each fiscal year, the Secretary shall reserve not less than 15 percent to make grants to covered entities for use carrying out in rural area projects for which Program funds may be used. (e) Allowable uses Recipients of a Program grant may use Program funds on the following: (1) Projects eligible for Federal assistance under section 5312. (2) Acquisition of equipment (including vehicles), acquisition (including by license) of software (including software automated driving systems and software for the operation or monitoring of autonomous vehicles), and updates to such software. (f) Project funding (1) Federal share Notwithstanding section 5311, the Federal share of a project carried out using Program funds may not exceed 80 percent of the estimated total cost of the project. (2) In-kind contributions The non-Federal share of the cost of a project carried out using Program funds may be provided in the form of in-kind contributions. (g) Other sources of Federal funds (1) In general Nothing in this section shall be construed to prohibit a Program grant recipient from receiving financial assistance under any other law for use in a project for which the grant is issued. (2) Combination permitted A project carried out using Program funding may receive funding under section 5307 or any other provision of law. (3) Government share Nothing in this subparagraph shall be construed to alter the Government share required under subsection (f), section 5307, or any other provision of law. (h) Authorization of appropriations There is authorized to be appropriated to the Secretary for use carrying out this section\u2014 (1) $60,000,000 for fiscal year 2027 to remain available through fiscal year 2030; and (2) $40,000,000 for fiscal year 2028 to remain available through fiscal year 2031. (i) Covered entity defined In this section, the term eligible recipient means\u2014 (1) an entity that is an eligible recipient under section 5339 or an entity described in section 5312(b)(2); and (2) a partnership, entered into through a contract that satisfies the competitive procurement process under section 5325, between an entity described in paragraph (1) and\u2014 (A) a private entity, including a transit vehicle manufacturer, for purposes of carrying out a project to accelerate the deployment of a covered shared mobility vehicle; or (B) a transit vehicle manufacturer for purpose of carrying out any project for which Program funds may be used under this section. .\n##### (c) Technical amendment\nThe table of sections in chapter 53 of title 49, United States Code, is amended by adding after the item relating to section 5340 the following:\n5341. Accelerating innovative mobility grant program. .\n##### (d) Rolling stock\nSection 3019(b)(1)(A) of the FAST Act ( 49 U.S.C. 5325 note) is amended\u2014\n**(1)**\nin clause (iv) by striking and at the end;\n**(2)**\nin clause (v) by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new clause:\n(vi) the term rolling stock and related equipment includes\u2014 (I) buses, vans, and cars; (II) software for automated driving systems in such buses, vans, and cars; (III) software for the operation or monitoring of autonomous vehicles, include autonomous buses, vans, and cars; and (IV) updates to software described in subclauses (II) and (III). .\n#### 3. Testing facilities for new bus models, including certain autonomous shared mobility vehicles\n##### (a) Bus testing facilities\nSection 5318 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a) to read as follows:\n(a) Facilities (1) In general (A) Bus models The Secretary shall maintain one facility for testing new bus models (other than a new bus model that is a covered shared mobility vehicle) for maintainability, reliability, safety, performance (including braking performance), structural integrity, fuel economy, emissions, and noise. (B) Covered shared mobility vehicles Not later than January 1, 2027, the Secretary shall establish and maintain not fewer than one facility for testing new covered shared mobility vehicles for maintainability, reliability, safety, performance (including braking performance), structural integrity, fuel economy, emissions, and noise. (2) Location The Secretary shall ensure that each facility established under paragraph (1)(B) be at a facility at which, as of the date of establishment, substantial road-based (including track-based) validation testing of vehicles equipped with automated driving systems occurs. ;\n**(2)**\nin subsection (b) by striking maintain the facility and insert maintain each facility under subsection (a)(1) ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking The person and inserting Each person ; and\n**(B)**\nby striking maintaining the facility and inserting maintaining a facility under subsection (a)(1) ;\n**(4)**\nin subsection (d) by striking the operator of the facility and inserting each operator of a facility under subsection (a)(1) ; and\n**(5)**\nin subsection (f) by striking new bus models and inserting new bus models (other than a new bus model that is a covered shared mobility vehicle) or new covered shared mobility vehicles, as applicable .\n##### (b) Timing of testing\nSection 5318(e) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking a bus of that model has and inserting prior to delivery and acceptance of the new bus model, a bus of such model has ; and\n**(ii)**\nby striking subsection (a) and inserting subsection (a)(1) ; and\n**(B)**\nin subparagraph (B)(i) by striking by the Secretary by rule and inserting by the Secretary in the final rule maintained under paragraph (2) such that the new bus model has received a passing aggregate score from the bus model scoring system under such final rule ; and\n**(2)**\nby striking paragraph (2) and inserting the following:\n(2) Bus test pass/fail standard The Secretary shall maintain a final rule that\u2014 (A) includes a bus model scoring system that results in a weighted, aggregate score that uses the testing categories described in subparagraphs (A) and (B) of subsection (a)(1) and accounts for the relative importance of each such testing category; and (B) establishes a pass/fail standard that uses the aggregate score described in the subparagraph (A). (3) Collaboration In developing a bus model scoring system under paragraph (2)(A), the Secretary shall work with each bus testing facility under subsection (a)(1), bus manufacturers, and transit agencies. (4) Non-warranty An aggregate test score issued for a new bus model pursuant to the final rule maintained pursuant to paragraph (2) is for use indicating only whether the amounts appropriated or otherwise made available under this chapter may be obligated or expended to acquire the new bus model and shall not be interpreted as a warranty or guarantee that the new bus model will meet any specific requirements of a purchaser. .\n##### (c) Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a final rule, or modify an existing final rule, to comply with section 5318(e)(2) of title 49, United States Code, as amended by this section and include in the final rule any modifications necessary to enable timely testing of covered shared mobility vehicles under section 5318(a)(1) of such title.\n#### 4. Amendments to allow certain grant funds to be used to acquire software for automated driving systems\n##### (a) Strengthening mobility and revolutionizing transportation grant program\nSection 25005(e)(2)(B)(vii) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 502 note) is amended by striking acquisition of equipment, including vehicles and inserting acquisition of equipment (including vehicles), acquisition (including by license) of software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software .\n##### (b) Fixed guideway capital investment grants\nSection 5309(b)(2) of title 49, United States Code, is amended by striking infill stations, and inserting infill stations, acquisition (including by license) of software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software, .\n##### (c) Grants for buses and bus facilities\nSection 5339 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)(A) by striking including and inserting including acquisition (including by license) of software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software, and ;\n**(2)**\nin subsection (b)(1)(A) by striking equipment and inserting equipment, including acquisition (including by license) of software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software ; and\n**(3)**\nin subsection (c)(1)(B)\u2014\n**(A)**\nin clause (i) by inserting before the semicolon , including acquisition (including by license) of related software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software ;\n**(B)**\nin clause (ii) by inserting before the semicolon , including acquisition (including by license) of related software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software ; and\n**(C)**\nin clause (iii) by inserting before the semicolon including acquisition (including by license) of related software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), updates to such software .\n##### (d) National infrastructure project assistance\nSection 6701(h)(1)(B) of title 49, United States Code, is amended by striking and operational improvements and inserting operational improvements, and acquisition (including by license) of software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles), and updates to such software .\n##### (e) Better Utilizing Investments to Leverage Development grant program\nSection 6702 of title 49, United States Code, is amended by adding at the end the following new subsection:\n(l) Acquisition of certain software In carrying out an eligible project for which a grant under the Program is awarded, an eligible entity may use grant funds to update or acquire (including by license) software (including software for automated driving systems and software for the operation or monitoring of autonomous vehicles) that is related to, or a component of, the eligible project. .",
      "versionDate": "2026-05-07",
      "versionType": "Introduced in House"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8692ih.xml"
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
      "title": "SAM Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAM Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shared Autonomous Mobility Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to allow certain grant funds issued by the Secretary of Transportation to be used for the deployment and purchasing of technology for certain autonomous shared mobility vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:34Z"
    }
  ]
}
```
