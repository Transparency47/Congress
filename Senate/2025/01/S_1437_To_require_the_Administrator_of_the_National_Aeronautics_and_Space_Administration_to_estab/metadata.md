# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1437
- Title: ASCEND Act
- Congress: 119
- Bill type: S
- Bill number: 1437
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-20T19:43:21Z
- Update date including text: 2026-04-20T19:43:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 173.
- 2025-12-09 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8581; text: CR S8581)
- 2025-12-09 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-10 - Floor: Message on Senate action sent to the House.
- 2025-12-10 12:03:50 - Floor: Received in the House.
- 2025-12-10 12:25:43 - Floor: Held at the desk.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 173.
- 2025-12-09 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8581; text: CR S8581)
- 2025-12-09 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-10 - Floor: Message on Senate action sent to the House.
- 2025-12-10 12:03:50 - Floor: Received in the House.
- 2025-12-10 12:25:43 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1437",
    "number": "1437",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "ASCEND Act",
    "type": "S",
    "updateDate": "2026-04-20T19:43:21Z",
    "updateDateIncludingText": "2026-04-20T19:43:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-10",
      "actionTime": "12:25:43",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-10",
      "actionTime": "12:03:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8581; text: CR S8581)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 173.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-68.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
        "item": [
          {
            "date": "2025-09-29T19:44:52Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-10T17:40:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1437\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Hickenlooper (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the National Aeronautics and Space Administration to establish a program to identify, evaluate, acquire, and disseminate commercial Earth remote sensing data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act .\n#### 2. Commercial satellite data\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nSection 60501 of title 51, United States Code, states that the goal for the Earth Science program of the National Aeronautics and Space Administration (referred to in this section as NASA ) shall be to pursue a program of Earth observations, research, and applications activities to better understand the Earth, how it supports life, and how human activities affect its ability to do so in the future.\n**(2)**\nSection 50115 of title 51, United States Code, states that the Administrator of NASA shall, to the extent possible and while satisfying the scientific or educational requirements of NASA, and where appropriate, of other Federal agencies and scientific researchers, acquire, where cost effective, space-based and airborne commercial Earth remote sensing data, services, distribution, and applications from a commercial provider.\n**(3)**\nThe Administrator of NASA established the Commercial SmallSat Data Acquisition Pilot Program in 2019 to identify, validate, and acquire from commercial sources data that support the Earth science research and application goals.\n**(4)**\nThe Administrator of NASA has\u2014\n**(A)**\ndetermined that the pilot program described in paragraph (3) has been a success, as described in the final evaluation entitled Commercial SmallSat Data Acquisition Program Pilot Evaluation Report issued in 2020;\n**(B)**\nestablished a formal process for evaluating and onboarding new commercial vendors in such pilot program;\n**(C)**\nincreased the number of commercial vendors and commercial data products available through such pilot program; and\n**(D)**\nexpanded procurement arrangements with commercial vendors to broaden user access to provide Earth remote sensing data and imagery to federally funded researchers.\n##### (b) Commercial Satellite Data Acquisition Program\n**(1) In general**\nChapter 603 of title 51, United States Code, is amended by adding at the end the following:\n60307. Commercial Satellite Data Acquisition Program (a) In general The Administrator shall establish within the Earth Science Division of the Science Mission Directorate a program to acquire and disseminate commercial Earth observation data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and where appropriate, of other Federal agencies and scientific researchers. (b) Data publication and transparency The terms and conditions of commercial Earth remote sensing data and imagery acquisitions under the program described in subsection (a) shall not prevent\u2014 (1) the publication of commercial data or imagery for scientific purposes; or (2) the publication of information that is derived from, incorporates, or enhances the original commercial data or imagery of a vendor. (c) Authorization (1) In general In carrying out the program under this section, the Administrator may\u2014 (A) procure commercial Earth remote sensing data and imagery from commercial vendors to advance scientific research and applications for the purpose set forth in subsection (a); and (B) establish or modify end-use license terms and conditions to allow for the widest possible use of procured commercial Earth remote sensing data and imagery by individuals other than NASA-funded users, consistent with the goals of the program. (2) Acquisition from United States vendors The commercial Earth remote sensing data and imagery procured under this subsection shall be procured, to the maximum extent practicable, from United States vendors. (d) Report Not later than 180 days after the date of the enactment of this section, and annually thereafter, the Administrator shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that includes the following: (1) (A) In the case of the initial report, a list of all vendors that are providing commercial Earth remote sensing data and imagery to NASA as of the date of the report. (B) For each subsequent report, a list of all vendors that have provided commercial Earth remote sensing data and imagery to NASA during the reporting period. (2) A description of the end-use license terms and conditions for each such vendor. (3) A description of the manner in which each such vendor is advancing scientific research and applications, including priorities recommended by the National Academies of Sciences, Engineering, and Medicine decadal surveys. (4) Information specifying whether the Administrator has entered into an agreement with a commercial vendor or a Federal agency that permits the use of data and imagery by Federal Government employees, contractors, or non-Federal users. (e) Definition of United States vendor In this section, the term United States vendor means a commercial or nonprofit entity incorporated in the United States. .\n**(2) Clerical amendment**\nThe table of contents for chapter 603 of title 51, United States Code, is amended by adding at the end the following new item:\n60307. Commercial Satellite Data Acquisition Program. .",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437rs.xml",
      "text": "II\nCalendar No. 173\n119th CONGRESS\n1st Session\nS. 1437\n[Report No. 119\u201368]\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Hickenlooper (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 29, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Administrator of the National Aeronautics and Space Administration to establish a program to identify, evaluate, acquire, and disseminate commercial Earth remote sensing data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act .\n#### 2. Commercial satellite data\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nSection 60501 of title 51, United States Code, states that the goal for the Earth Science program of the National Aeronautics and Space Administration (referred to in this section as NASA ) shall be to pursue a program of Earth observations, research, and applications activities to better understand the Earth, how it supports life, and how human activities affect its ability to do so in the future.\n**(2)**\nSection 50115 of title 51, United States Code, states that the Administrator of NASA shall, to the extent possible and while satisfying the scientific or educational requirements of NASA, and where appropriate, of other Federal agencies and scientific researchers, acquire, where cost effective, space-based and airborne commercial Earth remote sensing data, services, distribution, and applications from a commercial provider.\n**(3)**\nThe Administrator of NASA established the Commercial SmallSat Data Acquisition Pilot Program in 2019 to identify, validate, and acquire from commercial sources data that support the Earth science research and application goals.\n**(4)**\nThe Administrator of NASA has\u2014\n**(A)**\ndetermined that the pilot program described in paragraph (3) has been a success, as described in the final evaluation entitled Commercial SmallSat Data Acquisition Program Pilot Evaluation Report issued in 2020;\n**(B)**\nestablished a formal process for evaluating and onboarding new commercial vendors in such pilot program;\n**(C)**\nincreased the number of commercial vendors and commercial data products available through such pilot program; and\n**(D)**\nexpanded procurement arrangements with commercial vendors to broaden user access to provide Earth remote sensing data and imagery to federally funded researchers.\n##### (b) Commercial Satellite Data Acquisition Program\n**(1) In general**\nChapter 603 of title 51, United States Code, is amended by adding at the end the following:\n60307. Commercial Satellite Data Acquisition Program (a) In general The Administrator shall establish within the Earth Science Division of the Science Mission Directorate a program to acquire and disseminate commercial Earth observation data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and where appropriate, of other Federal agencies and scientific researchers. (b) Data publication and transparency The terms and conditions of commercial Earth remote sensing data and imagery acquisitions under the program described in subsection (a) shall not prevent\u2014 (1) the publication of commercial data or imagery for scientific purposes; or (2) the publication of information that is derived from, incorporates, or enhances the original commercial data or imagery of a vendor. (c) Authorization (1) In general In carrying out the program under this section, the Administrator may\u2014 (A) procure commercial Earth remote sensing data and imagery from commercial vendors to advance scientific research and applications for the purpose set forth in subsection (a); and (B) establish or modify end-use license terms and conditions to allow for the widest possible use of procured commercial Earth remote sensing data and imagery by individuals other than NASA-funded users, consistent with the goals of the program. (2) Acquisition from United States vendors The commercial Earth remote sensing data and imagery procured under this subsection shall be procured, to the maximum extent practicable, from United States vendors. (d) Report Not later than 180 days after the date of the enactment of this section, and annually thereafter, the Administrator shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that includes the following: (1) (A) In the case of the initial report, a list of all vendors that are providing commercial Earth remote sensing data and imagery to NASA as of the date of the report. (B) For each subsequent report, a list of all vendors that have provided commercial Earth remote sensing data and imagery to NASA during the reporting period. (2) A description of the end-use license terms and conditions for each such vendor. (3) A description of the manner in which each such vendor is advancing scientific research and applications, including priorities recommended by the National Academies of Sciences, Engineering, and Medicine decadal surveys. (4) Information specifying whether the Administrator has entered into an agreement with a commercial vendor or a Federal agency that permits the use of data and imagery by Federal Government employees, contractors, or non-Federal users. (e) Definition of United States vendor In this section, the term United States vendor means a commercial or nonprofit entity incorporated in the United States. .\n**(2) Clerical amendment**\nThe table of contents for chapter 603 of title 51, United States Code, is amended by adding at the end the following new item:\n60307. Commercial Satellite Data Acquisition Program. .",
      "versionDate": "2025-09-29",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1437\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require the Administrator of the National Aeronautics and Space Administration to establish a program to identify, evaluate, acquire, and disseminate commercial Earth remote sensing data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act .\n#### 2. Commercial satellite data\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nSection 60501 of title 51, United States Code, states that the goal for the Earth Science program of the National Aeronautics and Space Administration (referred to in this section as NASA ) shall be to pursue a program of Earth observations, research, and applications activities to better understand the Earth, how it supports life, and how human activities affect its ability to do so in the future.\n**(2)**\nSection 50115 of title 51, United States Code, states that the Administrator of NASA shall, to the extent possible and while satisfying the scientific or educational requirements of NASA, and where appropriate, of other Federal agencies and scientific researchers, acquire, where cost effective, space-based and airborne commercial Earth remote sensing data, services, distribution, and applications from a commercial provider.\n**(3)**\nAfter the completion of the Private-Sector Small Constellation Satellite Data Product Pilot launch in 2017, the Administrator of NASA established the Commercial SmallSat Data Acquisition Pilot Program in 2019 to identify, evaluate, validate, and acquire from commercial sources data that support the Earth science research and application goals.\n**(4)**\nThe Administrator of NASA has\u2014\n**(A)**\ndetermined that the pilot program described in paragraph (3) has been a success, as described in the final evaluation entitled Commercial SmallSat Data Acquisition Program Pilot Evaluation Report issued in 2020;\n**(B)**\nestablished a formal process for evaluating and onboarding new commercial vendors in such pilot program;\n**(C)**\nincreased the number of commercial vendors and commercial data products available through such pilot program; and\n**(D)**\nexpanded procurement arrangements with commercial vendors to broaden user access to provide Earth remote sensing data and imagery to federally funded researchers.\n##### (b) Commercial Satellite Data Acquisition Program\n**(1) In general**\nChapter 603 of title 51, United States Code, is amended by adding at the end the following:\n60307. Commercial Satellite Data Acquisition Program (a) In general The Administrator shall establish within the Earth Science Division of the Science Mission Directorate a program, to be known as the Commercial Satellite Data Acquisition Program , to cost-effectively acquire and disseminate commercial Earth observation data and imagery in order to complement the scientific, operational, and educational requirements of the Administration, and where appropriate, of other Federal agencies and scientific researchers. (b) Data publication and accessibility The terms and conditions of commercial Earth remote sensing data and imagery acquisitions under the program described in subsection (a) shall not prevent\u2014 (1) the publication of commercial data or imagery in academic or scientific articles, papers, or other similar publications for scientific purposes; or (2) the publication, in academic or scientific articles, papers, or other similar publications, of information that is derived from, incorporates, or enhances the original commercial data or imagery of a vendor. (c) Authorization (1) In general In carrying out the program under this section, the Administrator may\u2014 (A) procure commercial Earth remote sensing data and imagery from commercial vendors to advance scientific research and applications for the purpose set forth in subsection (a); and (B) establish or modify end-use license terms and conditions to allow for the widest possible use of procured commercial Earth remote sensing data and imagery by individuals other than NASA-funded users, consistent with the goals of the program. (2) Acquisition from United States vendors The commercial Earth remote sensing data and imagery procured under this subsection shall be procured, to the maximum extent practicable, from United States vendors. (d) Report Not later than 180 days after the date of the enactment of this section, and annually thereafter, the Administrator shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that includes the following: (1) (A) In the case of the initial report, a list of all vendors that are providing commercial Earth remote sensing data and imagery to NASA as of the date of the report. (B) For each subsequent report, a list of all vendors that have provided commercial Earth remote sensing data and imagery to NASA during the reporting period. (2) A description of the end-use license terms and conditions for each such vendor. (3) A description of the manner in which each such vendor is advancing scientific research and applications, including priorities recommended by the National Academies of Sciences, Engineering, and Medicine decadal surveys. (4) Information specifying whether the Administrator has entered into an agreement with a commercial vendor or a Federal agency that permits the use of data and imagery by Federal Government employees, contractors, or non-Federal users. (e) Definition of United States vendor In this section, the term United States vendor means a commercial or nonprofit entity incorporated in the United States. .\n**(2) Clerical amendment**\nThe table of contents for chapter 603 of title 51, United States Code, is amended by adding at the end the following new item:\n60307. Commercial Satellite Data Acquisition Program. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2025-05-20T17:04:00Z"
          },
          {
            "name": "Earth sciences",
            "updateDate": "2025-05-20T17:04:00Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2025-05-20T17:04:00Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-05-20T17:04:00Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2025-05-20T17:04:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-19T15:44:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
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
          "measure-id": "id119s1437",
          "measure-number": "1437",
          "measure-type": "s",
          "orig-publish-date": "2025-12-09",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1437v55",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-12-09",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act</strong></p><p>This bill provides statutory authority for the Commercial SmallSat Data Acquisition (CSDA) program run by the National Aeronautics and Space Administration (NASA). Through the CSDA program, NASA acquires remote sensing data and imagery from commercial satellites to support its Earth science research. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p><p>Under the bill, NASA may establish or modify end-use agreements to allow for broad use of data and imagery acquired under the program, including by individuals outside of NASA (e.g., other federal agencies). The terms of any data or imagery acquisition may not prevent the publication of such data or imagery for scientific purposes or the publication of information derived from it. To the extent practicable, NASA must acquire such data and imagery from U.S. vendors. \u00a0</p>"
        },
        "title": "ASCEND Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1437.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act</strong></p><p>This bill provides statutory authority for the Commercial SmallSat Data Acquisition (CSDA) program run by the National Aeronautics and Space Administration (NASA). Through the CSDA program, NASA acquires remote sensing data and imagery from commercial satellites to support its Earth science research. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p><p>Under the bill, NASA may establish or modify end-use agreements to allow for broad use of data and imagery acquired under the program, including by individuals outside of NASA (e.g., other federal agencies). The terms of any data or imagery acquisition may not prevent the publication of such data or imagery for scientific purposes or the publication of information derived from it. To the extent practicable, NASA must acquire such data and imagery from U.S. vendors. \u00a0</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s1437"
    },
    "title": "ASCEND Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Accessing Satellite Capabilities to Enable New Discoveries Act or the ASCEND Act</strong></p><p>This bill provides statutory authority for the Commercial SmallSat Data Acquisition (CSDA) program run by the National Aeronautics and Space Administration (NASA). Through the CSDA program, NASA acquires remote sensing data and imagery from commercial satellites to support its Earth science research. (<em>Remote sensing</em> generally refers to the collection of data by instruments in Earth\u2019s orbit, such as satellites, that can be processed into imagery of Earth\u2019s surface.)</p><p>Under the bill, NASA may establish or modify end-use agreements to allow for broad use of data and imagery acquired under the program, including by individuals outside of NASA (e.g., other federal agencies). The terms of any data or imagery acquisition may not prevent the publication of such data or imagery for scientific purposes or the publication of information derived from it. To the extent practicable, NASA must acquire such data and imagery from U.S. vendors. \u00a0</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s1437"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1437es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "ASCEND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ASCEND Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-10T04:23:23Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Accessing Satellite Capabilities to Enable New Discoveries Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-10T04:23:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Accessing Satellite Capabilities to Enable New Discoveries Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ASCEND Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ASCEND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T13:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accessing Satellite Capabilities to Enable New Discoveries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T13:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the National Aeronautics and Space Administration to establish a program to identify, evaluate, acquire, and disseminate commercial Earth remote sensing data and imagery in order to satisfy the scientific, operational, and educational requirements of the Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T13:03:19Z"
    }
  ]
}
```
