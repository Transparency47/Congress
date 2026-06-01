# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1890?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1890
- Title: Carla Walker Act
- Congress: 119
- Bill type: S
- Bill number: 1890
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-05-22T19:19:22Z
- Update date including text: 2026-05-22T19:19:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 419.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 419.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1890",
    "number": "1890",
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
    "title": "Carla Walker Act",
    "type": "S",
    "updateDate": "2026-05-22T19:19:22Z",
    "updateDateIncludingText": "2026-05-22T19:19:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 419.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-05-20",
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
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
            "date": "2026-05-20T19:38:50Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:59:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T18:19:39Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "VT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "ID"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1890is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1890\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cornyn (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program for certain State and local forensic activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Carla Walker Act .\n#### 2. Grants to improve forensic activities\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Grants to improve forensic activities 3061. Definitions In this part: (1) Forensic analysis The term forensic analysis means an expert examination or test\u2014 (A) required by a law enforcement agency, a prosecutor, a criminal suspect or defendant, or a relevant court; and (B) performed on physical evidence, including DNA evidence, for the purpose of determining the connection of the evidence to a criminal act. (2) Forensic laboratory The term forensic laboratory means a facility, entity, or site accredited or pursuing accreditation as described in section 3062(d)(1)(C)(iii) that\u2014 (A) offers or performs forensic analysis; and (B) follows relevant chain of custody requirements for authentication by an appropriate court. 3062. DNA analysis grants (a) Eligible entity defined In this section, the term eligible entity means\u2014 (1) a State; (2) a Tribal or local law enforcement agency; (3) a prosecutor\u2019s office with a forensic laboratory capability; (4) a medical examiner\u2019s office; and (5) a coroner\u2019s office. (b) Authorization of grants The Attorney General may award a competitive grant to an eligible entity for the purpose of using any technology used in a forensic laboratory\u2014 (1) in order to conduct whole genome sequencing technology to assess at least 100,000 genetic markers ; and (2) that is compatible with multiple genealogical databases permitted to be used by law enforcement agencies under this part to generate investigative leads for criminal investigations or unidentified human remains. (c) Applications An eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time and in such form as the Attorney General may require. (d) Use of grant (1) In general An eligible entity that receives a grant under this section shall use amounts from the grant for any of the following activities: (A) To carry out DNA analyses of samples collected under applicable legal authority using the technology described in subsection (b) if the submission of such samples to the Combined DNA Index System has failed to produce investigative leads. (B) To carry out DNA analyses of unidentified human remains reasonably believed by investigators to be the remains of a suspected homicide victim using the technology described in subsection (b) if submission of such samples to the Combined DNA Index System has failed to provide an identity. (C) To outsource an activity described in subparagraph (A) or (B) for the use of technology described in subsection (b) and searching to\u2014 (i) an accredited publicly funded forensic laboratory; (ii) an accredited nongovernmental forensic laboratory; or (iii) a nongovernmental forensic laboratory that attests to the Attorney General, in a manner that is legally binding and enforceable, that the nongovernmental forensic laboratory will prepare and apply for such accreditation not later than 2 years after the date on which the nongovernmental laboratory first receives a request for analysis from an eligible entity receiving a grant under this section. (2) DOJ policy An activity carried out using amounts from a grant under this section shall be carried out consistent with the policy of the Department of Justice entitled Interim Policy on Forensic Genealogical DNA Analysis and Searching and dated November 1, 2019, or any successor policy, including with respect to communication between custodial Combined DNA Index System laboratories and vendor laboratories. (e) Authorization of appropriations (1) In general There are authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of fiscal years 2025 through 2029. (2) Limitations on use (A) In general Amounts appropriated to carry out this section\u2014 (i) subject to subparagraph (B), shall only be made available to carry out forensic genetic genealogical analysis; and (ii) shall not be made available for staffing, training, travel, and equipment. (B) Administrative costs The Attorney General may use not more than 10 percent of amounts appropriated to carry out this section for administrative costs. 3063. Grants to purchase forensic equipment enabled for forensic genetic genealogy DNA analysis and searching (a) Eligible entity defined In this section, the term eligible entity means\u2014 (1) a publicly funded and accredited forensic laboratory; (2) a medical examiner's office; and (3) a coroner's office. (b) Authorization of grants The Attorney General may award a grant to an eligible entity for the purpose of purchasing equipment to deploy forensic genetic genealogical DNA analysis and searching to generate investigative leads for criminal investigations or unidentified human remains. (c) Applications An eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time and in such form as the Attorney General may require. (d) Use of funds An eligible entity that receives a grant under this section shall use amounts from the grant to purchase forensic equipment, including supplies, reagents, consumables, and validation expenses, to deploy forensic genetic genealogy techniques, as defined in the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy, as applicable. (e) Authorization of appropriations There are authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of fiscal years 2025 through 2029. 3064. Administrative provisions (a) Regulations The Attorney General may promulgate guidelines, regulations, and procedures to carry out this part, including guidelines, regulations, and procedures relating to the submission and review of applications for grants under sections 3062 and 3063. (b) Accountability (1) Records An eligible entity that receives a grant under this part shall maintain such records as the Attorney General may require to facilitate an effective audit relating to the receipt of the grant, the use of amounts from the grant, outsourcing activities, and compliance with section VIII, entitled Sample and Data Control and Disposition , of the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy. (2) Access For the purpose of conducting audits and examinations, the Attorney General shall have access to any book, document, or record of an eligible entity that receives a grant under this section, a State or unit of local government within which the eligible entity operates, and any entity to which the eligible entity outsources work using amounts from the grant if the Attorney General determines that the book, document, or record relates to\u2014 (A) the receipt of the grant; (B) the use of amounts from the grant; or (C) compliance with section VIII, entitled Sample and Data Control and Disposition , of the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy. (3) Suspension and debarment In carrying out this part, the Attorney General shall comply with part 180 of title 2, Code of Federal Regulations, or any successor regulation. 3065. Reports Not later than 1 year after the date on which an eligible entity receives a grant under section 3062 or 3063, the eligible entity shall submit to the Attorney General a report that includes\u2014 (1) the amount of funding the eligible entity receives from the grant each fiscal year; (2) the number of cases for which the eligible entity performed testing using forensic genealogical DNA analysis during the previous year; (3) the type of forensic genetic genealogical DNA testing performed by the eligible entity, including\u2014 (A) the name of any laboratory to which the eligible entity outsources the testing; (B) the type of equipment used for the testing; and (C) the results of the testing, such as whether the testing resulted in successful victim or perpetrator identification or no identification and the time it took to make the identification; (4) the number of cases in which forensic genetic genealogical DNA analysis\u2014 (A) resulted in a searchable profile in a publicly available genealogy database; (B) generated a victim or perpetrator identification; (C) did not generate a victim or perpetrator identification; and (D) directly resulted in an arrest or victim identification; and (5) the average number of days it took to make an identification between the date of sample submission for forensic genetic genealogical DNA testing and the date of delivery of test results to the requesting office or agency. .\n#### 3. DOJ report\nNot later than 2 years after the date of enactment of this Act, the Attorney General, in consultation with the Forensic Laboratory Needs Working Group of the National Institute of Justice, shall submit to Congress a report\u2014\n**(1)**\non the awards and practices reported the Attorney General under section 3064 of title I of the Omnibus Crime Control and Safe Streets Act of 1968, as added by this Act;\n**(2)**\non forensic genetic genealogy technologies and how best to implement forensic genetic genealogy into publicly funded forensic laboratories; and\n**(3)**\nthat includes recommendations for\u2014\n**(A)**\nimplementing forensic investigative genetic genealogy technology, including expected funding needs; and\n**(B)**\nnecessary regulations for the use of forensic investigative genetic genealogy technology.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1890rs.xml",
      "text": "II\nCalendar No. 419\n119th CONGRESS\n2d Session\nS. 1890\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cornyn (for himself, Mr. Welch , Mr. Crapo , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo establish a grant program for certain State and local forensic activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Carla Walker Act .\n#### 2. Grants to improve forensic activities\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Grants to improve forensic activities 3061. Definitions In this part: (1) Forensic analysis The term forensic analysis means an expert examination or test\u2014 (A) required by a law enforcement agency, a prosecutor, a criminal suspect or defendant, or a relevant court; and (B) performed on physical evidence, including DNA evidence, for the purpose of determining the connection of the evidence to a criminal act. (2) Forensic laboratory The term forensic laboratory means a facility, entity, or site accredited or pursuing accreditation as described in section 3062(d)(1)(C)(iii) that\u2014 (A) offers or performs forensic analysis; and (B) follows relevant chain of custody requirements for authentication by an appropriate court. 3062. DNA analysis grants (a) Eligible entity defined In this section, the term eligible entity means\u2014 (1) a State; (2) a Tribal or local law enforcement agency; (3) a prosecutor\u2019s office with a forensic laboratory capability; (4) a medical examiner\u2019s office; and (5) a coroner\u2019s office. (b) Authorization of grants The Attorney General may award a competitive grant to an eligible entity for the purpose of using any technology used in a forensic laboratory\u2014 (1) in order to conduct whole genome sequencing technology to assess at least 100,000 genetic markers ; and (2) that is compatible with multiple genealogical databases permitted to be used by law enforcement agencies under this part to generate investigative leads for criminal investigations or unidentified human remains. (c) Applications An eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time and in such form as the Attorney General may require. (d) Use of grant (1) In general An eligible entity that receives a grant under this section shall use amounts from the grant for any of the following activities: (A) To carry out DNA analyses of samples collected under applicable legal authority using the technology described in subsection (b) if the submission of such samples to the Combined DNA Index System has failed to produce investigative leads. (B) To carry out DNA analyses of unidentified human remains reasonably believed by investigators to be the remains of a suspected homicide victim using the technology described in subsection (b) if submission of such samples to the Combined DNA Index System has failed to provide an identity. (C) To outsource an activity described in subparagraph (A) or (B) for the use of technology described in subsection (b) and searching to\u2014 (i) an accredited publicly funded forensic laboratory; (ii) an accredited nongovernmental forensic laboratory; or (iii) a nongovernmental forensic laboratory that attests to the Attorney General, in a manner that is legally binding and enforceable, that the nongovernmental forensic laboratory will prepare and apply for such accreditation not later than 2 years after the date on which the nongovernmental laboratory first receives a request for analysis from an eligible entity receiving a grant under this section. (2) DOJ policy An activity carried out using amounts from a grant under this section shall be carried out consistent with the policy of the Department of Justice entitled Interim Policy on Forensic Genealogical DNA Analysis and Searching and dated November 1, 2019, or any successor policy, including with respect to communication between custodial Combined DNA Index System laboratories and vendor laboratories. (e) Authorization of appropriations (1) In general There are authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of fiscal years 2025 through 2029. (2) Limitations on use (A) In general Amounts appropriated to carry out this section\u2014 (i) subject to subparagraph (B), shall only be made available to carry out forensic genetic genealogical analysis; and (ii) shall not be made available for staffing, training, travel, and equipment. (B) Administrative costs The Attorney General may use not more than 10 percent of amounts appropriated to carry out this section for administrative costs. 3063. Grants to purchase forensic equipment enabled for forensic genetic genealogy DNA analysis and searching (a) Eligible entity defined In this section, the term eligible entity means\u2014 (1) a publicly funded and accredited forensic laboratory; (2) a medical examiner's office; and (3) a coroner's office. (b) Authorization of grants The Attorney General may award a grant to an eligible entity for the purpose of purchasing equipment to deploy forensic genetic genealogical DNA analysis and searching to generate investigative leads for criminal investigations or unidentified human remains. (c) Applications An eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time and in such form as the Attorney General may require. (d) Use of funds An eligible entity that receives a grant under this section shall use amounts from the grant to purchase forensic equipment, including supplies, reagents, consumables, and validation expenses, to deploy forensic genetic genealogy techniques, as defined in the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy, as applicable. (e) Authorization of appropriations There are authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of fiscal years 2025 through 2029. 3064. Administrative provisions (a) Regulations The Attorney General may promulgate guidelines, regulations, and procedures to carry out this part, including guidelines, regulations, and procedures relating to the submission and review of applications for grants under sections 3062 and 3063. (b) Accountability (1) Records An eligible entity that receives a grant under this part shall maintain such records as the Attorney General may require to facilitate an effective audit relating to the receipt of the grant, the use of amounts from the grant, outsourcing activities, and compliance with section VIII, entitled Sample and Data Control and Disposition , of the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy. (2) Access For the purpose of conducting audits and examinations, the Attorney General shall have access to any book, document, or record of an eligible entity that receives a grant under this section, a State or unit of local government within which the eligible entity operates, and any entity to which the eligible entity outsources work using amounts from the grant if the Attorney General determines that the book, document, or record relates to\u2014 (A) the receipt of the grant; (B) the use of amounts from the grant; or (C) compliance with section VIII, entitled Sample and Data Control and Disposition , of the Interim Policy on Forensic Genealogical DNA Analysis and Search of the Department of Justice dated November 1, 2019, or any successor policy. (3) Suspension and debarment In carrying out this part, the Attorney General shall comply with part 180 of title 2, Code of Federal Regulations, or any successor regulation. 3065. Reports Not later than 1 year after the date on which an eligible entity receives a grant under section 3062 or 3063, the eligible entity shall submit to the Attorney General a report that includes\u2014 (1) the amount of funding the eligible entity receives from the grant each fiscal year; (2) the number of cases for which the eligible entity performed testing using forensic genealogical DNA analysis during the previous year; (3) the type of forensic genetic genealogical DNA testing performed by the eligible entity, including\u2014 (A) the name of any laboratory to which the eligible entity outsources the testing; (B) the type of equipment used for the testing; and (C) the results of the testing, such as whether the testing resulted in successful victim or perpetrator identification or no identification and the time it took to make the identification; (4) the number of cases in which forensic genetic genealogical DNA analysis\u2014 (A) resulted in a searchable profile in a publicly available genealogy database; (B) generated a victim or perpetrator identification; (C) did not generate a victim or perpetrator identification; and (D) directly resulted in an arrest or victim identification; and (5) the average number of days it took to make an identification between the date of sample submission for forensic genetic genealogical DNA testing and the date of delivery of test results to the requesting office or agency. .\n#### 3. DOJ report\nNot later than 2 years after the date of enactment of this Act, the Attorney General, in consultation with the Forensic Laboratory Needs Working Group of the National Institute of Justice, shall submit to Congress a report\u2014\n**(1)**\non the awards and practices reported the Attorney General under section 3064 of title I of the Omnibus Crime Control and Safe Streets Act of 1968, as added by this Act;\n**(2)**\non forensic genetic genealogy technologies and how best to implement forensic genetic genealogy into publicly funded forensic laboratories; and\n**(3)**\nthat includes recommendations for\u2014\n**(A)**\nimplementing forensic investigative genetic genealogy technology, including expected funding needs; and\n**(B)**\nnecessary regulations for the use of forensic investigative genetic genealogy technology.",
      "versionDate": "2025-05-22",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3591",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Carla Walker Act",
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
            "updateDate": "2026-05-22T19:19:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-22T19:19:16Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2026-05-22T19:18:43Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2026-05-22T19:18:57Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2026-05-22T19:19:22Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-05-22T19:19:11Z"
          },
          {
            "name": "Genetics",
            "updateDate": "2026-05-22T19:18:53Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-22T19:19:06Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2026-05-22T19:18:47Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-05-22T19:18:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-03T15:30:14Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1890is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1890rs.xml"
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
      "title": "Carla Walker Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "title": "Carla Walker Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Carla Walker Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program for certain State and local forensic activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:19Z"
    }
  ]
}
```
