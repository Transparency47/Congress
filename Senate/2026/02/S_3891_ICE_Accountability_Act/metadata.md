# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3891
- Title: ICE Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3891
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-03-02T16:06:56Z
- Update date including text: 2026-03-02T16:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3891",
    "number": "3891",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "ICE Accountability Act",
    "type": "S",
    "updateDate": "2026-03-02T16:06:56Z",
    "updateDateIncludingText": "2026-03-02T16:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T21:13:55Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3891is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3891\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Coons (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish an independent commission within the legislative branch responsible for ensuring oversight, transparency, and accountability in immigration enforcement operations.\n#### 1. Short title\nThis Act may be cited as the ICE Accountability Act .\n#### 2. Definitions\nIn this Act:\n**(1) Applicable requirements**\nThe term applicable requirements means all constitutional, statutory, regulatory, policy, and other requirements relating to the civil rights and civil liberties of individuals affected by the activities of immigration agencies, including such requirements under the Department of Homeland Security Appropriations Act, 2026 or a subsequent Department of Homeland Security appropriations Act.\n**(2) Commission**\nThe term Commission means the Commission for Independent Monitoring of Immigration Enforcement established under section 3.\n**(3) Immigration agency**\nThe term immigration agency means Immigration and Customs Enforcement, U.S. Customs and Border Protection, and any other agency employing agents temporarily or permanently tasked with engaging in immigration enforcement.\n**(4) Whistleblower**\nThe term whistleblower means an employee of an immigration agency who provides information to the Commission regarding conduct that the whistleblower reasonably believes constitutes an alleged violation of the applicable requirements.\n#### 3. Commission for Independent Monitoring of Immigration Enforcement\n##### (a) Establishment\nThere is hereby established in the legislative branch an independent commission, to be known as the Commission for Independent Monitoring of Immigration Enforcement.\n##### (b) Purposes\nThe purposes of the Commission are\u2014\n**(1)**\nto ensure rigorous, independent oversight of immigration agencies\u2019 compliance with applicable requirements;\n**(2)**\nto investigate whether immigration agencies have failed to comply with applicable requirements; and\n**(3)**\nto ensure public transparency of immigration enforcement operations.\n##### (c) Duties\nThe Commission shall\u2014\n**(1)**\nmonitor immigration agencies during immigration enforcement activities related to arrest, detention, deportation, and surveillance operations, including by\u2014\n**(A)**\nobserving agents during operations; and\n**(B)**\nconducting on-site visits, which may be conducted without notice, provided that the Commission makes good faith efforts to provide advance notice of on-site visits and activities to immigration agencies if the Commission determines that advance notice is practicable, appropriate, and would not undermine the goals of its oversight;\n**(2)**\nreview any information and data, including encounter documents, training materials, civil rights complaints, body camera footage, and other records, in possession of the Department of Homeland Security pertaining to immigration enforcement activities;\n**(3)**\nissue monthly reports to Congress that contain evaluations of immigration agencies\u2019 compliance with applicable requirements, and make all such reports publicly accessible;\n**(4)**\nmaintain a publicly accessible website that\u2014\n**(A)**\nallows members of the public to upload complaints;\n**(B)**\nallows, as the Commission deems appropriate and consistent with applicable law, members of the public to view anonymized complaint information;\n**(C)**\ncontains detailed data released by the Commission related to immigration agencies\u2019 enforcement actions, disaggregated by geographic location; and\n**(D)**\ncontains all reports and findings issued by the Commission;\n**(5)**\npromptly review complaints submitted by members of the public to inform findings;\n**(6)**\nif approved by a vote of at least 3 of 4 monitors\u2014\n**(A)**\nissue formal findings of serious or willful violations of applicable requirements;\n**(B)**\nrefer matters to the Department of Justice recommending prosecution under section 242 of title 18, United States Code, or to a State attorney general recommending prosecution under State law, upon findings indicating potential criminal conduct;\n**(C)**\nhold public hearings about potential violations of applicable requirements;\n**(D)**\ninitiate a civil action in accordance with section 4(b) to seek enforcement of the applicable requirements; and\n**(E)**\nmake recommendations to Congress for reforms to immigration enforcement operations and ways to strengthen immigration enforcement oversight by the Department of Homeland Security's Office of Inspector General, Office for Civil Rights and Civil Liberties, and Office of the Immigration Detention Ombudsman based on the Commission\u2019s findings; and\n**(7)**\nat the request of the Chair or Ranking Member of the Committee on the Judiciary of the Senate , the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on the Judiciary of the House of Representatives , the Committee on Homeland Security of the House of Representatives , or the Committee on Oversight and Government Reform of the House of Representatives , and at least quarterly, testify to Congress on the Commission's findings and recommendations.\n##### (d) Authorities\n**(1) Access to department of homeland security systems**\nThe Commission is entitled to access, without prior notice, in a reasonable manner that, consistent with the Commission\u2019s responsibilities, minimizes interference with daily operations, to monitor and observe all Department of Homeland Security records, facilities and other property, trainings, meetings, incident scenes, and personnel that\u2014\n**(A)**\nare relevant to immigration enforcement; and\n**(B)**\nthe Commission reasonably considers necessary to carry out its duties.\n**(2) Subpoena power**\nThe Commission is authorized, by a vote of at least 3 of 4 monitors, to subpoena witness testimony and all records in the possession of the Department of Homeland Security related to the Department's compliance or noncompliance with applicable requirements, in case of a violation by the Department of its obligations to ensure the Commission's access to Department systems.\n**(3) Consultation with external experts**\nThe Commission may procure the temporary and intermittent services of external experts in accordance with section 3109(b) of title 5, United States Code, including in the process of developing its monitoring methodology, evaluation metrics, and standards for determining a serious or willful violation of applicable requirements.\n**(4) Contracting authority**\nThe Commission may expend funds appropriated to the Commission to enter into contracts that enable the Commission to discharge its duties under this section.\n**(5) Civil action**\nThe Commission may select attorneys to bring a civil action against an immigration agency\u2014\n**(A)**\nto enforce subpoenas issued pursuant to paragraph (2) and access requirements described in section 7(a); and\n**(B)**\nto seek a judicial order described in section 4(b).\n#### 4. Judicial enforcement\n##### (a) Civil action\n**(1) In general**\nIf the Commission determines that an immigration agency has engaged in a serious or willful violation of applicable requirements, the Commission is authorized, through attorneys selected by the Commission, to bring a civil action in the United States District Court for the District of Columbia against any immigration agency.\n**(2) Judicial order**\nThe court referred to in paragraph (1) is authorized to impose penalties pursuant to subsection (b) or to issue any decree, judgment, or order that may be necessary or appropriate to ensure the immigration agency complies with all applicable requirements.\n##### (b) Penalties\nAn immigration agency that has engaged in a serious or willful violation of applicable requirements shall be subject to a penalty equal to $500,000 for each day such agency remains out of compliance with such requirements.\n##### (c) Liability of immigration agency for agents\u2019 actions\nThe noncompliance of any individual agent shall be imputed to the immigration agency that supervises such agent.\n#### 5. Personnel\n##### (a) Appointment of monitors\nNot later than 30 days after the date of the enactment of this Act, 4 monitors shall be appointed to the Commission, of whom\u2014\n**(1)**\n1 monitor shall be appointed by the Speaker of the House of Representatives, with the consent of the minority leader of the House of Representatives;\n**(2)**\n1 monitor shall be appointed by the minority leader of the House of Representatives, with the consent of the Speaker of the House of Representatives;\n**(3)**\n1 monitor shall be appointed by the majority leader of the Senate, with the consent of the minority leader of the Senate; and\n**(4)**\n1 monitor shall be appointed by the minority leader of the Senate, with the consent of the majority leader of the Senate.\n##### (b) Qualifications\n**(1) Expertise**\nEach monitor shall have significant depth of experience and nationally recognized expertise in a relevant field, such as civil rights enforcement (including rights guaranteed under the First, Fourth, and Fourteenth Amendments to the Constitution of the United States), law enforcement best practices, immigration law, Department of Homeland Security operations, and monitoring and evaluation.\n**(2) Nongovernmental appointees**\nNo monitor appointed to the Commission, no Executive Director, and no staff of the Commission may hold any other office or employment with the Federal Government or any State or local government while working for the Commission.\n**(3) Conflict of interest**\nNo individual serving as a monitor, no Executive Director, and no staff of the Commission may have any conflict of interest with respect to any aspect of performing their duties and responsibilities on the Commission.\n**(4) Eligibility for security clearances**\nEvery monitor and staff member shall\u2014\n**(A)**\nbe eligible to receive a security clearance of a level adequate to access all Department of Homeland Security systems that the Commission determines to be relevant to carrying out its duties; or\n**(B)**\nif the monitor or staff member lacks the requisite security clearance, begin the process of obtaining a security clearance upon joining the Commission.\n**(5) Training**\nEach monitor and staff member shall receive training on protecting the integrity of ongoing and future civil and criminal investigations into matters under the Commission\u2019s purview.\n##### (c) Term\nEach monitor shall serve a 5-year term. If a monitor departs before the end of his or her term, a new monitor shall be appointed in his or her place within 30 days of such departure, using the same appointment process as used for the departing monitor.\n##### (d) Compensation\nEach monitor shall perform full-time services and be paid at the annual rate of basic pay for level I of the Executive Schedule.\n##### (e) Staffing\n**(1) In general**\nThe Commission, at the direction of the Executive Director, shall hire appropriate staff members to enable the Commission to carry out its duties.\n**(2) Executive director**\nNot later than 30 days after all monitors have been appointed to the Commission, the monitors shall jointly select an individual with demonstrated, nationally recognized expertise in law enforcement best practices to serve as Executive Director of the Commission and to guide the daily operations of the Commission\u2019s monitoring functions.\n#### 6. Sunset provision\n##### (a) In general\nNot earlier than 4 years after the date of the enactment of this Act and not later than 180 days after at least 3 of the 4 monitors of the Commission determine that the immigration agencies have all been in substantial compliance with the applicable requirements for at least 1 year, the Commission shall terminate operations.\n##### (b) Pause on sunsetting\nIf, after a determination described in subsection (a) is made and before the Commission terminates operations, the Commission determines that 1 or more of the immigration agencies are no longer in substantial compliance with the applicable requirements, the Commission may reverse the decision to terminate operations by a vote of at least 3 of the 4 monitors.\n#### 7. Obligations of Federal agencies\n##### (a) Department of Homeland Security\nThe Secretary of Homeland Security shall\u2014\n**(1)**\npermit and facilitate the Commission\u2019s prompt access to all Department of Homeland Security records, personnel, and facilities, including facilities operated or owned by a contractor of the Department;\n**(2)**\ndesignate an office in the Department charged with liaising with the Commission and ensuring adherence with all provisions of this Act; and\n**(3)**\nnotify the Commission as soon as practicable, and in no case more than 12 hours after the event, of any critical firearm discharge, in-custody death, or death during an encounter with an immigration officer.\n##### (b) General Services Administration\nThe Administrator of General Services shall provide to the Commission, on a reimbursable basis, administrative support and other services for the performance of the Commission\u2019s functions. Office facilities provided to the Commission under this subsection may not be shared with an entity of the executive branch.\n##### (c) Security clearances\nAny agency involved in reviewing applications for, granting, or revoking security clearances shall perform such functions for members and staff of the Commission in the same manner as they are performed for other Federal personnel.\n##### (d) Prohibition against retaliation\n**(1) In general**\nA Federal employee may not (directly or indirectly) discharge, demote, suspend, threaten, blacklist, harass, or in any other manner discriminate against a whistleblower because of any lawful act done by the whistleblower in\u2014\n**(A)**\nproviding information to the Commission regarding any conduct that the whistleblower reasonably believes constitutes an alleged violation of the applicable requirements; or\n**(B)**\ninitiating, testifying in, or assisting in any Commission process, or preparing to take any such action.\n**(2) Enforcement**\nIn addition to any other remedies otherwise available, the rights, procedures, and remedies under section 5323 of title 31, United States Code, are available and shall apply to a judicial or administrative action based on or related to information provided by a whistleblower in the same manner as such rights, procedures, and remedies apply to a covered judicial or administrative action under that section.\n#### 8. Authorization of appropriations\nThere is authorized to be appropriated to the Commission such sums as may be necessary for each fiscal year during which the Commission operates.\n#### 9. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any other person or circumstance, shall not be affected.",
      "versionDate": "2026-02-12",
      "versionType": "Introduced in Senate"
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
        "name": "Immigration",
        "updateDate": "2026-03-02T16:06:56Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3891is.xml"
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
      "title": "ICE Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T03:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ICE Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an independent commission within the legislative branch responsible for ensuring oversight, transparency, and accountability in immigration enforcement operations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:23Z"
    }
  ]
}
```
