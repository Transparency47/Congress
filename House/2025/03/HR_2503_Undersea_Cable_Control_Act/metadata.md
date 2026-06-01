# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2503
- Title: Undersea Cable Control Act
- Congress: 119
- Bill type: HR
- Bill number: 2503
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-09-05T04:08:19Z
- Update date including text: 2025-09-05T04:08:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by Voice Vote.
- 2025-09-02 16:45:03 - Floor: Mr. Baumgartner moved to suspend the rules and pass the bill.
- 2025-09-02 16:45:20 - Floor: Considered under suspension of the rules. (consideration: CR H3733-3734)
- 2025-09-02 16:45:22 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 2503.
- 2025-09-02 16:51:56 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H3733-3734: 1)
- 2025-09-02 16:51:56 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.
- 2025-09-02 16:52:00 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-09-03 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by Voice Vote.
- 2025-09-02 16:45:03 - Floor: Mr. Baumgartner moved to suspend the rules and pass the bill.
- 2025-09-02 16:45:20 - Floor: Considered under suspension of the rules. (consideration: CR H3733-3734)
- 2025-09-02 16:45:22 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 2503.
- 2025-09-02 16:51:56 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H3733-3734: 1)
- 2025-09-02 16:51:56 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.
- 2025-09-02 16:52:00 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-09-03 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2503",
    "number": "2503",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Undersea Cable Control Act",
    "type": "HR",
    "updateDate": "2025-09-05T04:08:19Z",
    "updateDateIncludingText": "2025-09-05T04:08:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-09-02",
      "actionTime": "16:52:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-09-02",
      "actionTime": "16:51:56",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H3733-3734: 1)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-09-02",
      "actionTime": "16:51:56",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-09-02",
      "actionTime": "16:45:22",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 2503.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-09-02",
      "actionTime": "16:45:20",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H3733-3734)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-09-02",
      "actionTime": "16:45:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Baumgartner moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-09-03T21:50:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": [
          {
            "date": "2025-04-09T14:46:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-31T16:05:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2503\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Kean introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the development of a strategy to eliminate the availability to foreign adversaries of goods and technologies capable of supporting undersea cables, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Undersea Cable Control Act .\n#### 2. Strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables\n##### (a) In general\nThe President, acting through the Secretary of Commerce and in coordination with the Secretary of State, shall develop a strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables consistent with United States policy described in section 1752 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 ).\n##### (b) Matters To be included\nThe strategy required under subsection (a) shall include the following:\n**(1)**\nAn identification of items required for supporting the construction, maintenance, or operation of an undersea cable project.\n**(2)**\nAn identification of United States and multilateral export controls and licensing policies for items identified pursuant to paragraph (1) with respect to foreign adversaries.\n**(3)**\nAn identification of United States allies and partners that have a share of the global market with respect to the items so identified, including a detailed description of the availability of such items without restriction in sufficient quantities and comparable in quality to those produced in the United States.\n**(4)**\nA description of ongoing negotiations with other countries to achieve unified export controls and licensing policies for items so identified to eliminate availability to foreign adversaries.\n**(5)**\nTo the extent practicable, an identification of all identified entities under the control, ownership, or influence of a foreign adversary that support the construction, operation, or maintenance of undersea cables.\n**(6)**\nA description of efforts taken to promote United States leadership at international standards-setting bodies for equipment, systems, software, and virtually defined networks relevant to undersea cables, taking into account the different processes followed by such bodies.\n**(7)**\nA description of the presence and activities of foreign adversaries at international standards-setting bodies relevant to undersea cables, including information on the differences in the scope and scale of the engagement of foreign adversaries at such bodies compared to engagement at such bodies by the United States and its allies and partners, and the security risks raised by the proposals of foreign adversaries at such bodies.\n##### (c) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report that contains the strategy required under subsection (a).\n**(2) Form**\nEach report required under this subsection shall\u2014\n**(A)**\nbe submitted in unclassified form, but may contain a classified annex; and\n**(B)**\nbe made available on a publicly accessible Federal Government website.\n##### (d) Agreement\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the President shall seek to\u2014\n**(A)**\nestablish bilateral or multilateral agreements with allies and partners identified pursuant to subsection (b)(3) to seek to eliminate the availability to foreign adversaries of items identified pursuant to subsection (b)(1); and\n**(B)**\ninclude in such agreements penalty provisions for noncompliance.\n**(2) Briefings**\nThe President shall brief the congressional committees specified in subsection (c)(1) on negotiations to establish agreements described in paragraph (1) beginning not later than 30 days after receipt of the report required under subsection (a) and every 180 days thereafter until each such agreement is established.\n##### (e) Actions\n**(1) In general**\nThe Secretary of Commerce shall evaluate the export, reexport, and in-country transfer of the items identified pursuant to subsection (b)(1) for appropriate controls under the Export Administration Regulations, including by evaluating, for each item so identified, whether to add the technology to the Commerce Control List maintained under title 15, Code of Federal Regulations.\n**(2) Levels of control**\n**(A) In general**\nIn determining the level of control appropriate for items identified pursuant to subsection (b)(1), including requirements for a license or other authorization for the export, reexport, or in-country transfer of any such technology, the Secretary of Commerce (in coordination with the Secretary of Defense, the Secretary of State, and the heads of other Federal agencies, as appropriate) shall take into account the potential end uses and end users of the item.\n**(B) Statement of policy**\nAt a minimum, it is the policy of the United States to work with its allies and partners to control the export, reexport, or in-country transfer of technologies identified pursuant to subsection (b)(1) to or in a country subject to an embargo, including an arms embargo, imposed by the United States.\n**(3) Notification**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for 3 years, the President, acting through the Secretary of Commerce, shall submit to the appropriate congressional committees an unclassified notification describing the results of actions taken pursuant to this subsection in the preceding period, including a description of\u2014\n**(A)**\nthe individual items evaluated for controls; and\n**(B)**\nthe rationale, including United States national security and foreign policy considerations, for adding or not adding an item to the Commerce Control List maintained under title 15, Code of Federal Regulations, pursuant to the evaluation under paragraph (1) with respect to such item.\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Foreign adversary**\nThe term foreign adversary has the meaning given such term in section 8(c) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1607(c) ).\n**(3) Item**\nThe term item has the meaning given such term in the Export Administration Regulations (15 C.F.R. 772.1).",
      "versionDate": "2025-03-31",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 2503\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Received; read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nAN ACT\nTo require the development of a strategy to eliminate the availability to foreign adversaries of goods and technologies capable of supporting undersea cables, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Undersea Cable Control Act .\n#### 2. Strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables\n##### (a) In general\nThe President, acting through the Secretary of Commerce and in coordination with the Secretary of State, shall develop a strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables consistent with United States policy described in section 1752 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 ).\n##### (b) Matters To be included\nThe strategy required under subsection (a) shall include the following:\n**(1)**\nAn identification of items required for supporting the construction, maintenance, or operation of an undersea cable project.\n**(2)**\nAn identification of United States and multilateral export controls and licensing policies for items identified pursuant to paragraph (1) with respect to foreign adversaries.\n**(3)**\nAn identification of United States allies and partners that have a share of the global market with respect to the items so identified, including a detailed description of the availability of such items without restriction in sufficient quantities and comparable in quality to those produced in the United States.\n**(4)**\nA description of ongoing negotiations with other countries to achieve unified export controls and licensing policies for items so identified to eliminate availability to foreign adversaries.\n**(5)**\nTo the extent practicable, an identification of all identified entities under the control, ownership, or influence of a foreign adversary that support the construction, operation, or maintenance of undersea cables.\n**(6)**\nA description of efforts taken to promote United States leadership at international standards-setting bodies for equipment, systems, software, and virtually defined networks relevant to undersea cables, taking into account the different processes followed by such bodies.\n**(7)**\nA description of the presence and activities of foreign adversaries at international standards-setting bodies relevant to undersea cables, including information on the differences in the scope and scale of the engagement of foreign adversaries at such bodies compared to engagement at such bodies by the United States and its allies and partners, and the security risks raised by the proposals of foreign adversaries at such bodies.\n##### (c) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report that contains the strategy required under subsection (a).\n**(2) Form**\nEach report required under this subsection shall\u2014\n**(A)**\nbe submitted in unclassified form, but may contain a classified annex; and\n**(B)**\nbe made available on a publicly accessible Federal Government website.\n##### (d) Agreement\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the President shall seek to\u2014\n**(A)**\nestablish bilateral or multilateral agreements with allies and partners identified pursuant to subsection (b)(3) to seek to eliminate the availability to foreign adversaries of items identified pursuant to subsection (b)(1); and\n**(B)**\ninclude in such agreements penalty provisions for noncompliance.\n**(2) Briefings**\nThe President shall brief the congressional committees specified in subsection (c)(1) on negotiations to establish agreements described in paragraph (1) beginning not later than 30 days after receipt of the report required under subsection (a) and every 180 days thereafter until each such agreement is established.\n##### (e) Actions\n**(1) In general**\nThe Secretary of Commerce shall evaluate the export, reexport, and in-country transfer of the items identified pursuant to subsection (b)(1) for appropriate controls under the Export Administration Regulations, including by evaluating, for each item so identified, whether to add the technology to the Commerce Control List maintained under title 15, Code of Federal Regulations.\n**(2) Levels of control**\n**(A) In general**\nIn determining the level of control appropriate for items identified pursuant to subsection (b)(1), including requirements for a license or other authorization for the export, reexport, or in-country transfer of any such technology, the Secretary of Commerce (in coordination with the Secretary of Defense, the Secretary of State, and the heads of other Federal agencies, as appropriate) shall take into account the potential end uses and end users of the item.\n**(B) Statement of policy**\nAt a minimum, it is the policy of the United States to work with its allies and partners to control the export, reexport, or in-country transfer of technologies identified pursuant to subsection (b)(1) to or in a country subject to an embargo, including an arms embargo, imposed by the United States.\n**(3) Notification**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for 3 years, the President, acting through the Secretary of Commerce, shall submit to the appropriate congressional committees an unclassified notification describing the results of actions taken pursuant to this subsection in the preceding period, including a description of\u2014\n**(A)**\nthe individual items evaluated for controls; and\n**(B)**\nthe rationale, including United States national security and foreign policy considerations, for adding or not adding an item to the Commerce Control List maintained under title 15, Code of Federal Regulations, pursuant to the evaluation under paragraph (1) with respect to such item.\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Foreign adversary**\nThe term foreign adversary has the meaning given such term in section 8(c) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1607(c) ).\n**(3) Item**\nThe term item has the meaning given such term in the Export Administration Regulations (15 CFR 772.1).",
      "versionDate": "2025-09-03",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2503\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo require the development of a strategy to eliminate the availability to foreign adversaries of goods and technologies capable of supporting undersea cables, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Undersea Cable Control Act .\n#### 2. Strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables\n##### (a) In general\nThe President, acting through the Secretary of Commerce and in coordination with the Secretary of State, shall develop a strategy to eliminate the availability to foreign adversaries of items required for supporting undersea cables consistent with United States policy described in section 1752 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 ).\n##### (b) Matters To be included\nThe strategy required under subsection (a) shall include the following:\n**(1)**\nAn identification of items required for supporting the construction, maintenance, or operation of an undersea cable project.\n**(2)**\nAn identification of United States and multilateral export controls and licensing policies for items identified pursuant to paragraph (1) with respect to foreign adversaries.\n**(3)**\nAn identification of United States allies and partners that have a share of the global market with respect to the items so identified, including a detailed description of the availability of such items without restriction in sufficient quantities and comparable in quality to those produced in the United States.\n**(4)**\nA description of ongoing negotiations with other countries to achieve unified export controls and licensing policies for items so identified to eliminate availability to foreign adversaries.\n**(5)**\nTo the extent practicable, an identification of all identified entities under the control, ownership, or influence of a foreign adversary that support the construction, operation, or maintenance of undersea cables.\n**(6)**\nA description of efforts taken to promote United States leadership at international standards-setting bodies for equipment, systems, software, and virtually defined networks relevant to undersea cables, taking into account the different processes followed by such bodies.\n**(7)**\nA description of the presence and activities of foreign adversaries at international standards-setting bodies relevant to undersea cables, including information on the differences in the scope and scale of the engagement of foreign adversaries at such bodies compared to engagement at such bodies by the United States and its allies and partners, and the security risks raised by the proposals of foreign adversaries at such bodies.\n##### (c) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report that contains the strategy required under subsection (a).\n**(2) Form**\nEach report required under this subsection shall\u2014\n**(A)**\nbe submitted in unclassified form, but may contain a classified annex; and\n**(B)**\nbe made available on a publicly accessible Federal Government website.\n##### (d) Agreement\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the President shall seek to\u2014\n**(A)**\nestablish bilateral or multilateral agreements with allies and partners identified pursuant to subsection (b)(3) to seek to eliminate the availability to foreign adversaries of items identified pursuant to subsection (b)(1); and\n**(B)**\ninclude in such agreements penalty provisions for noncompliance.\n**(2) Briefings**\nThe President shall brief the congressional committees specified in subsection (c)(1) on negotiations to establish agreements described in paragraph (1) beginning not later than 30 days after receipt of the report required under subsection (a) and every 180 days thereafter until each such agreement is established.\n##### (e) Actions\n**(1) In general**\nThe Secretary of Commerce shall evaluate the export, reexport, and in-country transfer of the items identified pursuant to subsection (b)(1) for appropriate controls under the Export Administration Regulations, including by evaluating, for each item so identified, whether to add the technology to the Commerce Control List maintained under title 15, Code of Federal Regulations.\n**(2) Levels of control**\n**(A) In general**\nIn determining the level of control appropriate for items identified pursuant to subsection (b)(1), including requirements for a license or other authorization for the export, reexport, or in-country transfer of any such technology, the Secretary of Commerce (in coordination with the Secretary of Defense, the Secretary of State, and the heads of other Federal agencies, as appropriate) shall take into account the potential end uses and end users of the item.\n**(B) Statement of policy**\nAt a minimum, it is the policy of the United States to work with its allies and partners to control the export, reexport, or in-country transfer of technologies identified pursuant to subsection (b)(1) to or in a country subject to an embargo, including an arms embargo, imposed by the United States.\n**(3) Notification**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for 3 years, the President, acting through the Secretary of Commerce, shall submit to the appropriate congressional committees an unclassified notification describing the results of actions taken pursuant to this subsection in the preceding period, including a description of\u2014\n**(A)**\nthe individual items evaluated for controls; and\n**(B)**\nthe rationale, including United States national security and foreign policy considerations, for adding or not adding an item to the Commerce Control List maintained under title 15, Code of Federal Regulations, pursuant to the evaluation under paragraph (1) with respect to such item.\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Foreign adversary**\nThe term foreign adversary has the meaning given such term in section 8(c) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1607(c) ).\n**(3) Item**\nThe term item has the meaning given such term in the Export Administration Regulations (15 CFR 772.1).",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
            "name": "Asia",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "China",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Technology transfer and commercialization",
            "updateDate": "2025-05-14T17:37:45Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-05-14T17:37:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-13T19:40:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2503",
          "measure-number": "2503",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-09-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2503v00",
            "update-date": "2025-09-02"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Undersea Cable Control Act</strong></p><p>This bill requires the President and the Department of Commerce to take certain actions to prevent foreign adversaries from acquiring items needed to support the construction, maintenance, or operation of undersea cable projects. For the purposes of this bill, a<em> foreign adversary</em> is any foreign government or nongovernment person (entity or individual) engaged in certain conduct that significantly and adversely affects U.S. national security.</p><p>Within one year of the bill's enactment,\u00a0the President must seek to enter into agreements with allies and partners to prevent such items from being available to foreign adversaries.</p><p>Furthermore, Commerce must determine the appropriate level of export and transfer controls for such items under the Export Administration Regulations.</p><p>The bill also requires Commerce to develop a strategy to prevent such items from being available to foreign adversaries. The President must report annually to Congress on this strategy.</p>"
        },
        "title": "Undersea Cable Control Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2503.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Undersea Cable Control Act</strong></p><p>This bill requires the President and the Department of Commerce to take certain actions to prevent foreign adversaries from acquiring items needed to support the construction, maintenance, or operation of undersea cable projects. For the purposes of this bill, a<em> foreign adversary</em> is any foreign government or nongovernment person (entity or individual) engaged in certain conduct that significantly and adversely affects U.S. national security.</p><p>Within one year of the bill's enactment,\u00a0the President must seek to enter into agreements with allies and partners to prevent such items from being available to foreign adversaries.</p><p>Furthermore, Commerce must determine the appropriate level of export and transfer controls for such items under the Export Administration Regulations.</p><p>The bill also requires Commerce to develop a strategy to prevent such items from being available to foreign adversaries. The President must report annually to Congress on this strategy.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119hr2503"
    },
    "title": "Undersea Cable Control Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Undersea Cable Control Act</strong></p><p>This bill requires the President and the Department of Commerce to take certain actions to prevent foreign adversaries from acquiring items needed to support the construction, maintenance, or operation of undersea cable projects. For the purposes of this bill, a<em> foreign adversary</em> is any foreign government or nongovernment person (entity or individual) engaged in certain conduct that significantly and adversely affects U.S. national security.</p><p>Within one year of the bill's enactment,\u00a0the President must seek to enter into agreements with allies and partners to prevent such items from being available to foreign adversaries.</p><p>Furthermore, Commerce must determine the appropriate level of export and transfer controls for such items under the Export Administration Regulations.</p><p>The bill also requires Commerce to develop a strategy to prevent such items from being available to foreign adversaries. The President must report annually to Congress on this strategy.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119hr2503"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2503eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Undersea Cable Control Act",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-09-05T04:08:19Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Undersea Cable Control Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-09-04T02:08:18Z"
    },
    {
      "title": "Undersea Cable Control Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Undersea Cable Control Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the development of a strategy to eliminate the availability to foreign adversaries of goods and technologies capable of supporting undersea cables, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:03:15Z"
    }
  ]
}
```
