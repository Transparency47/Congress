# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4394
- Title: Promoting Police Leadership Act
- Congress: 119
- Bill type: S
- Bill number: 4394
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-21T20:38:27Z
- Update date including text: 2026-05-21T20:38:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 414.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 414.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4394",
    "number": "4394",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Promoting Police Leadership Act",
    "type": "S",
    "updateDate": "2026-05-21T20:38:27Z",
    "updateDateIncludingText": "2026-05-21T20:38:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 414.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
            "date": "2026-05-19T18:49:22Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:59:11Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-27T22:03:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "RI"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "SC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "AZ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4394is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4394\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Cornyn (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to improve the COPS program with respect to training command-level personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Police Leadership Act .\n#### 2. Commander curriculum development\n##### (a) Definitions\nSection 901(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a) ) is amended\u2014\n**(1)**\nin paragraph (32), by striking and at the end;\n**(2)**\nin paragraph (33), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(34) the term command-level personnel means law enforcement officers employed by a State, local, or Tribal law enforcement agency whose responsibilities include managing, directing, or overseeing law enforcement operations within a geographic subunit of the jurisdiction in which such agency has primary responsibility for law enforcement activities. .\n##### (b) COPS program\nSection 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended by adding at the end the following:\n(q) Training in improving police command-Level personnel leadership, management, and effectiveness (1) Training curricula (A) In general Not later than 180 days after the date of enactment of this subsection, the Attorney General shall develop training curricula or identify effective existing training curricula for command-level personnel relating to\u2014 (i) leadership and strategic thinking; (ii) critical incident response and management, including understanding, preparing for, and responding to the effect of critical incidents on officers and communities; (iii) risk management; (iv) officer wellness; (v) data analysis and data-driven policing tactics; (vi) evidence-based decision making; and (vii) building community trust. (B) Requirements The training curricula developed or identified under this paragraph shall include\u2014 (i) primarily in-person instruction and peer-to-peer learning; (ii) a framework for a practical, evidence-based problem solving component under which participating command-level personnel\u2014 (I) identify and develop a proposed solution to a leadership, operational, or management challenge relevant to personnel in the command-level personnel\u2019s employing law enforcement agency; (II) receive feedback from curriculum instructors and other participating command-level personnel to refine the proposed solution accordingly to meet the needs of the law enforcement agency and community served; and (III) present a final, implementable product emphasizing evidence-based strategies to program instructors and the command-level personnel\u2019s district or geographic command; and (iii) the incorporation of pre-course and post-course assessments to measure knowledge acquisition and leadership competencies relevant to the training curricula. (C) Consultation The Attorney General shall develop and identify training curricula under this paragraph in consultation with relevant law enforcement agencies of States and units of local government, universities with appropriate law-enforcement or leadership programs, and any other entities the Attorney General determines appropriate. (2) Certified programs and courses (A) In general Not later than 180 days after the date on which training curricula are developed or identified under paragraph (1), the Attorney General shall establish a process to\u2014 (i) certify training programs and courses offered to command-level personnel which incorporate 1 or more of the training curricula developed or identified under paragraph (1), or equivalents to such training curricula, which may include certifying training programs or courses offered on or before the date on which the Attorney General establishes the process; and (ii) terminate the certification of a training program or course that fails to meet the standards developed or identified under paragraph (1). (B) Partnerships with educational institutions Not later than 180 days after the date on which training curricula are developed or identified under paragraph (1), the Attorney General shall develop criteria to ensure that entities which offer training programs or courses that are certified under subparagraph (A) collaborate with educational institutions to evaluate and continuously improve the curricula and coursework of those educational institutions. (3) List Not later than 1 year after the date on which the Attorney General completes the activities required under paragraphs (1) and (2), the Attorney General shall publish a list of law enforcement agencies of States and units of local government employing law enforcement officers who have successfully completed a course using the training curricula developed or identified under paragraph (1), or equivalents to such training curricula, which shall include\u2014 (A) the total number of law enforcement officers that are employed by the law enforcement agency; and (B) the number of law enforcement officers who have completed such a course. .\n#### 3. Attorney General reports\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, and annually thereafter until the date that is 3 years after the date of enactment of this Act, the Attorney General shall submit to Congress a report on the activities carried out as a result of the amendments made under section 2.\n**(2) Contents**\nEach report under paragraph (1) shall include, at a minimum, information on\u2014\n**(A)**\nsteps taken by the Attorney General to develop or identify curricula under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2;\n**(B)**\nany assessments conducted or identified by the Attorney General on the effectiveness and utilization of curricula developed or identified under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2;\n**(C)**\nrecommendations for curriculum updates and improvements; and\n**(D)**\nbarriers to training implementation.\n#### 4. GAO report\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct a review of the actions taken by the Attorney General pursuant to this Act and the amendments made by this Act; and\n**(2)**\nsubmit to Congress a report on the review conducted under paragraph (1), which shall include a description of\u2014\n**(A)**\nthe process for developing and identifying curricula under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2, including the effectiveness of the consultation by the Attorney General with the agencies, associations, and organizations identified under that section; and\n**(B)**\nthe certification of training programs and courses under section 1701(q)(2) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2, including the development of the process for certification and its implementation.\n#### 5. State certifications and training standards\nNothing in this Act, or an amendment made by this Act, shall be construed to preempt or replace the authority of any State or local government, including any Peace Officer Standards and Training entity or similar certifying body, to set and enforce certification, training, or qualification standards for law enforcement officers.",
      "versionDate": "2026-04-27",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4394rs.xml",
      "text": "II\nCalendar No. 414\n119th CONGRESS\n2d Session\nS. 4394\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Cornyn (for himself, Mr. Whitehouse , Mr. Graham , Mr. Durbin , Mrs. Blackburn , Mrs. Capito , Mr. Kelly , Mr. Blumenthal , Mr. Cruz , Ms. Hirono , Ms. Klobuchar , Mr. Padilla , Mr. Tillis , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 19, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to improve the COPS program with respect to training command-level personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Police Leadership Act .\n#### 2. Commander curriculum development\n##### (a) Definitions\nSection 901(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a) ) is amended\u2014\n**(1)**\nin paragraph (32), by striking and at the end;\n**(2)**\nin paragraph (33), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(34) the term command-level personnel means law enforcement officers employed by a State, local, or Tribal law enforcement agency whose responsibilities include managing, directing, or overseeing law enforcement operations within a geographic subunit of the jurisdiction in which such agency has primary responsibility for law enforcement activities. .\n##### (b) COPS program\nSection 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended by adding at the end the following:\n(q) Training in improving police command-Level personnel leadership, management, and effectiveness (1) Training curricula (A) In general Not later than 180 days after the date of enactment of this subsection, the Attorney General shall develop training curricula or identify effective existing training curricula for command-level personnel relating to\u2014 (i) leadership and strategic thinking; (ii) critical incident response and management, including understanding, preparing for, and responding to the effect of critical incidents on officers and communities; (iii) risk management; (iv) officer wellness; (v) data analysis and data-driven policing tactics; (vi) evidence-based decision making; and (vii) building community trust. (B) Requirements The training curricula developed or identified under this paragraph shall include\u2014 (i) primarily in-person instruction and peer-to-peer learning; (ii) a framework for a practical, evidence-based problem solving component under which participating command-level personnel\u2014 (I) identify and develop a proposed solution to a leadership, operational, or management challenge relevant to personnel in the command-level personnel\u2019s employing law enforcement agency; (II) receive feedback from curriculum instructors and other participating command-level personnel to refine the proposed solution accordingly to meet the needs of the law enforcement agency and community served; and (III) present a final, implementable product emphasizing evidence-based strategies to program instructors and the command-level personnel\u2019s district or geographic command; and (iii) the incorporation of pre-course and post-course assessments to measure knowledge acquisition and leadership competencies relevant to the training curricula. (C) Consultation The Attorney General shall develop and identify training curricula under this paragraph in consultation with relevant law enforcement agencies of States and units of local government, universities with appropriate law-enforcement or leadership programs, and any other entities the Attorney General determines appropriate. (2) Certified programs and courses (A) In general Not later than 180 days after the date on which training curricula are developed or identified under paragraph (1), the Attorney General shall establish a process to\u2014 (i) certify training programs and courses offered to command-level personnel which incorporate 1 or more of the training curricula developed or identified under paragraph (1), or equivalents to such training curricula, which may include certifying training programs or courses offered on or before the date on which the Attorney General establishes the process; and (ii) terminate the certification of a training program or course that fails to meet the standards developed or identified under paragraph (1). (B) Partnerships with educational institutions Not later than 180 days after the date on which training curricula are developed or identified under paragraph (1), the Attorney General shall develop criteria to ensure that entities which offer training programs or courses that are certified under subparagraph (A) collaborate with educational institutions to evaluate and continuously improve the curricula and coursework of those educational institutions. (3) List Not later than 1 year after the date on which the Attorney General completes the activities required under paragraphs (1) and (2), the Attorney General shall publish a list of law enforcement agencies of States and units of local government employing law enforcement officers who have successfully completed a course using the training curricula developed or identified under paragraph (1), or equivalents to such training curricula, which shall include\u2014 (A) the total number of law enforcement officers that are employed by the law enforcement agency; and (B) the number of law enforcement officers who have completed such a course. .\n#### 3. Attorney General reports\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, and annually thereafter until the date that is 3 years after the date of enactment of this Act, the Attorney General shall submit to Congress a report on the activities carried out as a result of the amendments made under section 2.\n**(2) Contents**\nEach report under paragraph (1) shall include, at a minimum, information on\u2014\n**(A)**\nsteps taken by the Attorney General to develop or identify curricula under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2;\n**(B)**\nany assessments conducted or identified by the Attorney General on the effectiveness and utilization of curricula developed or identified under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2;\n**(C)**\nrecommendations for curriculum updates and improvements; and\n**(D)**\nbarriers to training implementation.\n#### 4. GAO report\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct a review of the actions taken by the Attorney General pursuant to this Act and the amendments made by this Act; and\n**(2)**\nsubmit to Congress a report on the review conducted under paragraph (1), which shall include a description of\u2014\n**(A)**\nthe process for developing and identifying curricula under section 1701(q)(1) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2, including the effectiveness of the consultation by the Attorney General with the agencies, associations, and organizations identified under that section; and\n**(B)**\nthe certification of training programs and courses under section 1701(q)(2) of the Omnibus Crime Control and Safe Streets Act of 1968, as added by section 2, including the development of the process for certification and its implementation.\n#### 5. State certifications and training standards\nNothing in this Act, or an amendment made by this Act, shall be construed to preempt or replace the authority of any State or local government, including any Peace Officer Standards and Training entity or similar certifying body, to set and enforce certification, training, or qualification standards for law enforcement officers.",
      "versionDate": "2026-05-19",
      "versionType": "Reported in Senate"
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
        "updateDate": "2026-05-18T14:34:22Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4394is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4394rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Promoting Police Leadership Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-21T20:38:27Z"
    },
    {
      "title": "Promoting Police Leadership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Police Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T05:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to improve the COPS program with respect to training command-level personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T05:33:29Z"
    }
  ]
}
```
