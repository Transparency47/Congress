# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/668
- Title: Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 668
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2026-02-05T01:06:13Z
- Update date including text: 2026-02-05T01:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-02 - IntroReferral: Submitted in House
- 2025-09-02 - IntroReferral: Submitted in House
- 2025-09-03 14:06:59 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House.
- 2025-09-03 14:06:59 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House. (consideration: CR H3780; text: CR H3780)
- Latest action: 2025-09-02: Submitted in House

## Actions

- 2025-09-02 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-02 - IntroReferral: Submitted in House
- 2025-09-02 - IntroReferral: Submitted in House
- 2025-09-03 14:06:59 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House.
- 2025-09-03 14:06:59 - Floor: Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House. (consideration: CR H3780; text: CR H3780)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/668",
    "number": "668",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "J000311",
        "district": "3",
        "firstName": "Brian",
        "fullName": "Rep. Jack, Brian [R-GA-3]",
        "lastName": "Jack",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-02-05T01:06:13Z",
    "updateDateIncludingText": "2026-02-05T01:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-09-03",
      "actionTime": "14:06:59",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House. (consideration: CR H3780; text: CR H3780)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-09-03",
      "actionTime": "14:06:59",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Pursuant to the provisions of H. Res. 672, H. Res. 668 is considered passed House.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-09-02T16:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "GA"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "SC"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres668ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 668\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Mr. Jack (for himself, Ms. Foxx , Mr. Griffith , Mr. Langworthy , Mrs. Houchin , Mrs. Fischbach , Mr. Austin Scott of Georgia , Mr. Norman , and Mr. Roy ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nDirecting the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government\u2019s investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.\n#### 1. Committee on Oversight and Government Reform Epstein Investigation\nThe Committee on Oversight and Government Reform is directed to continue its ongoing investigation into the possible mismanagement of the Federal Government\u2019s investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, the circumstances and subsequent investigations of Mr. Epstein\u2019s death, the operation of sex-trafficking rings and ways for the Federal Government to effectively combat them, and potential violations of ethics rules related to elected officials in order to inform, among other things, legislative solutions to improve Federal efforts to combat sex trafficking and reform the use of non-prosecution agreements and plea agreements in sex-crime investigations.\n#### 2. Investigative proceedings by the Committee on Oversight and Government Reform\n##### (a) In general\nThe House of Representatives supports the subpoenas and investigatory actions authorized by the chair of the Committee on Oversight and Government Reform as of the date of the adoption of this resolution with respect to the investigation described in section 1 and encourages all recipients to fully comply with them in a timely manner.\n##### (b) Issuance of investigative reports\nThe Committee on Oversight and Government Reform shall issue such investigative reports with respect to the investigation described in section 1 as it deems necessary.\n#### 3. Release of documents relating to Jeffrey Epstein\n##### (a) In general\nThe chair of the Committee on Oversight and Government Reform shall make publicly available all unclassified committee records received from the Attorney General, the Secretary of the Treasury, and the Epstein estate, and any other custodians related to the investigation described in this resolution, as well as any written declarations, or other evidence that relates to the investigation described in this resolution, including those referring or relating to any of the following:\n**(1)**\nJeffrey Epstein, including all investigations, prosecutions, or custodial matters.\n**(2)**\nGhislaine Maxwell.\n**(3)**\nFlight logs or travel records, including but not limited to manifests, itineraries, pilot records, and customs or immigration documentation for any aircraft, vessel, or vehicle owned, operated, or used by Jeffrey Epstein or any related entity.\n**(4)**\nIndividuals, including government officials, named or referenced in connection with Epstein\u2019s criminal activities, civil settlements, immunity or plea agreements, or investigatory proceedings.\n**(5)**\nEntities (corporate, nonprofit, academic, or governmental) with known or alleged ties to Epstein\u2019s trafficking or financial networks.\n**(6)**\nAny immunity deals, non-prosecution agreements, plea bargains, or sealed settlements involving Epstein or his associates.\n**(7)**\nInternal DOJ communications, including emails, memos, and meeting notes, concerning decisions to charge, not charge, investigate, or decline to investigate Epstein or his associates.\n**(8)**\nAll communications, memoranda, directives, logs, or metadata concerning the destruction, deletion, alteration, misplacement, or concealment of documents, recordings, or electronic data related to Epstein, his associates, his detention and death, or any investigative files.\n**(9)**\nDocumentation of Epstein\u2019s detention or death, including incident reports, witness interviews, medical examiner files, autopsy reports, and written records detailing the circumstances and cause of death.\n##### (b) Withholding, delay, or redaction\n**(1) Prohibited grounds**\nNo committee record described in subsection (a) shall be withheld, delayed, or redacted on the basis of embarrassment, reputational harm, or political sensitivity, including with respect to any government official, public figure, or foreign dignitary.\n**(2) Permitted withholdings or redactions**\n**(A) In general**\nThe chair of the Committee on Oversight and Government Reform may withhold or redact the segregable portions of committee records described in subsection (a) that\u2014\n**(i)**\ncontain personally identifiable information of victims or victims\u2019 personal and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy together with materials that could likely be used or reconstituted to unveil and identify a victim;\n**(ii)**\ndepict or contain child pornography, other child sexual abuse materials, or similar materials;\n**(iii)**\nwould jeopardize an active Federal investigation or ongoing prosecution, including whistleblower investigations, provided that such withholding is narrowly tailored and temporary;\n**(iv)**\ndepict or contain images of death, physical abuse, or injury of any person; or\n**(v)**\ncontain information specifically authorized under criteria established by law or executive order to be kept secret in the interest of national defense or foreign policy and are in fact properly classified pursuant to such law or executive order.\n**(B) Written justification requirement**\n**(i) In general**\nAll withholdings or redactions made by the chair under subparagraph (A) shall be accompanied by a written justification for such withholding or redaction accompanying the release.\n**(ii) Record custodian written justification**\nIf the chair of the Committee on Oversight and Government Reform receives any records described in subsection (a) that already include redactions or if the chair knows any of the records described in such subsection are being withheld, the chair shall request the custodian of such records to provide written justifications for each redaction or withholding, and shall make each such justification publicly available promptly upon receipt.",
      "versionDate": "2025-09-02",
      "versionType": "IH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres668eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 668\nIn the House of Representatives, U. S.,\nSeptember 3, 2025\nRESOLUTION\nDirecting the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government\u2019s investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.\n#### 1. Committee on Oversight and Government Reform Epstein Investigation\nThe Committee on Oversight and Government Reform is directed to continue its ongoing investigation into the possible mismanagement of the Federal Government\u2019s investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, the circumstances and subsequent investigations of Mr. Epstein\u2019s death, the operation of sex-trafficking rings and ways for the Federal Government to effectively combat them, and potential violations of ethics rules related to elected officials in order to inform, among other things, legislative solutions to improve Federal efforts to combat sex trafficking and reform the use of non-prosecution agreements and plea agreements in sex-crime investigations.\n#### 2. Investigative proceedings by the Committee on Oversight and Government Reform\n##### (a) In general\nThe House of Representatives supports the subpoenas and investigatory actions authorized by the chair of the Committee on Oversight and Government Reform as of the date of the adoption of this resolution with respect to the investigation described in section 1 and encourages all recipients to fully comply with them in a timely manner.\n##### (b) Issuance of investigative reports\nThe Committee on Oversight and Government Reform shall issue such investigative reports with respect to the investigation described in section 1 as it deems necessary.\n#### 3. Release of documents relating to Jeffrey Epstein\n##### (a) In general\nThe chair of the Committee on Oversight and Government Reform shall make publicly available all unclassified committee records received from the Attorney General, the Secretary of the Treasury, and the Epstein estate, and any other custodians related to the investigation described in this resolution, as well as any written declarations, or other evidence that relates to the investigation described in this resolution, including those referring or relating to any of the following:\n**(1)**\nJeffrey Epstein, including all investigations, prosecutions, or custodial matters.\n**(2)**\nGhislaine Maxwell.\n**(3)**\nFlight logs or travel records, including but not limited to manifests, itineraries, pilot records, and customs or immigration documentation for any aircraft, vessel, or vehicle owned, operated, or used by Jeffrey Epstein or any related entity.\n**(4)**\nIndividuals, including government officials, named or referenced in connection with Epstein\u2019s criminal activities, civil settlements, immunity or plea agreements, or investigatory proceedings.\n**(5)**\nEntities (corporate, nonprofit, academic, or governmental) with known or alleged ties to Epstein\u2019s trafficking or financial networks.\n**(6)**\nAny immunity deals, non-prosecution agreements, plea bargains, or sealed settlements involving Epstein or his associates.\n**(7)**\nInternal DOJ communications, including emails, memos, and meeting notes, concerning decisions to charge, not charge, investigate, or decline to investigate Epstein or his associates.\n**(8)**\nAll communications, memoranda, directives, logs, or metadata concerning the destruction, deletion, alteration, misplacement, or concealment of documents, recordings, or electronic data related to Epstein, his associates, his detention and death, or any investigative files.\n**(9)**\nDocumentation of Epstein\u2019s detention or death, including incident reports, witness interviews, medical examiner files, autopsy reports, and written records detailing the circumstances and cause of death.\n##### (b) Withholding, delay, or redaction\n**(1) Prohibited grounds**\nNo committee record described in subsection (a) shall be withheld, delayed, or redacted on the basis of embarrassment, reputational harm, or political sensitivity, including with respect to any government official, public figure, or foreign dignitary.\n**(2) Permitted withholdings or redactions**\n**(A) In general**\nThe chair of the Committee on Oversight and Government Reform may withhold or redact the segregable portions of committee records described in subsection (a) that\u2014\n**(i)**\ncontain personally identifiable information of victims or victims\u2019 personal and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy together with materials that could likely be used or reconstituted to unveil and identify a victim;\n**(ii)**\ndepict or contain child pornography, other child sexual abuse materials, or similar materials;\n**(iii)**\nwould jeopardize an active Federal investigation or ongoing prosecution, including whistleblower investigations, provided that such withholding is narrowly tailored and temporary;\n**(iv)**\ndepict or contain images of death, physical abuse, or injury of any person; or\n**(v)**\ncontain information specifically authorized under criteria established by law or executive order to be kept secret in the interest of national defense or foreign policy and are in fact properly classified pursuant to such law or executive order.\n**(B) Written justification requirement**\n**(i) In general**\nAll withholdings or redactions made by the chair under subparagraph (A) shall be accompanied by a written justification for such withholding or redaction accompanying the release.\n**(ii) Record custodian written justification**\nIf the chair of the Committee on Oversight and Government Reform receives any records described in subsection (a) that already include redactions or if the chair knows any of the records described in such subsection are being withheld, the chair shall request the custodian of such records to provide written justifications for each redaction or withholding, and shall make each such justification publicly available promptly upon receipt.",
      "versionDate": "2025-09-03",
      "versionType": "EH"
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
        "actionDate": "2025-09-03",
        "actionTime": "14:06:12",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "672",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Procedurally related"
        }
      },
      "title": "Providing for consideration of the bill (H.R. 4553) making appropriations for energy and water development and related agencies for the fiscal year ending September 30, 2026, and for other purposes; providing for consideration of the joint resolution (H.J. Res. 104) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Miles City Field Office Record of Decision and Approved Resource Management Plan Amendment''; providing for consideration of the joint resolution (H.J. Res. 105) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''North Dakota Field Office Record of Decision and Approved Resource Management Plan''; providing for consideration of the joint resolution (H.J. Res. 106) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Central Yukon Record of Decision and Approved Resource Management Plan''; and for other purposes.",
      "type": "HRES"
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
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-09-08T20:00:37Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-09-08T20:00:42Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-09-08T20:00:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-08T20:00:32Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-08T20:00:18Z"
          },
          {
            "name": "House Committee on Oversight and Government Reform",
            "updateDate": "2025-09-08T20:00:25Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-09-08T20:00:51Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-09-08T20:00:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-03T12:54:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-02",
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
          "measure-id": "id119hres668",
          "measure-number": "668",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-02",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres668v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-09-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution directs the Committee on Oversight and Government Reform\u00a0to continue its investigation into the federal government's investigation of Jeffrey Epstein and Ghislaine Maxwell and to release to the public committee records relating to the committee's investigation, subject to limited exceptions.</p><p>Under the resolution, the committee\u00a0records to be publicly disclosed include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein;\u00a0individuals named in connection with\u00a0Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.</p><p>The resolution\u00a0provides that the committee may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. The committee may not withhold or redact\u00a0records on the basis of embarrassment, reputational harm, or political sensitivity.</p><p>The resolution states support for the committee's subpoenas and investigatory actions and encourages timely compliance with them. Additionally, the committee shall issue investigative reports as it deems\u00a0necessary.</p>"
        },
        "title": "Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres668.xml",
    "summary": {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution directs the Committee on Oversight and Government Reform\u00a0to continue its investigation into the federal government's investigation of Jeffrey Epstein and Ghislaine Maxwell and to release to the public committee records relating to the committee's investigation, subject to limited exceptions.</p><p>Under the resolution, the committee\u00a0records to be publicly disclosed include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein;\u00a0individuals named in connection with\u00a0Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.</p><p>The resolution\u00a0provides that the committee may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. The committee may not withhold or redact\u00a0records on the basis of embarrassment, reputational harm, or political sensitivity.</p><p>The resolution states support for the committee's subpoenas and investigatory actions and encourages timely compliance with them. Additionally, the committee shall issue investigative reports as it deems\u00a0necessary.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hres668"
    },
    "title": "Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution directs the Committee on Oversight and Government Reform\u00a0to continue its investigation into the federal government's investigation of Jeffrey Epstein and Ghislaine Maxwell and to release to the public committee records relating to the committee's investigation, subject to limited exceptions.</p><p>Under the resolution, the committee\u00a0records to be publicly disclosed include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein;\u00a0individuals named in connection with\u00a0Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.</p><p>The resolution\u00a0provides that the committee may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. The committee may not withhold or redact\u00a0records on the basis of embarrassment, reputational harm, or political sensitivity.</p><p>The resolution states support for the committee's subpoenas and investigatory actions and encourages timely compliance with them. Additionally, the committee shall issue investigative reports as it deems\u00a0necessary.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hres668"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres668ih.xml"
        }
      ],
      "type": "IH"
    },
    {
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres668eh.xml"
        }
      ],
      "type": "EH"
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
      "title": "Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T08:18:19Z"
    },
    {
      "title": "Directing the Committee on Oversight and Government Reform to continue its ongoing investigation into the possible mismanagement of the Federal government's investigation of Mr. Jeffrey Epstein and Ms. Ghislaine Maxwell, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T08:05:25Z"
    }
  ]
}
```
