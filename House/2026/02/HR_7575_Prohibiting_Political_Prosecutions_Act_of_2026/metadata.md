# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7575
- Title: Prohibiting Political Prosecutions Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7575
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-03-09T19:20:00Z
- Update date including text: 2026-03-09T19:20:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-13: Introduced in House

## Actions

- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7575",
    "number": "7575",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Prohibiting Political Prosecutions Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T19:20:00Z",
    "updateDateIncludingText": "2026-03-09T19:20:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
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
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-13",
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
          "date": "2026-02-13T15:00:05Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "DC"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7575ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7575\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Mr. Goldman of New York introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to prohibit attorneys for the Government from being influenced by the political association, activities, or beliefs of a person in determining whether to commence or recommend prosecution or take other action against the person.\n#### 1. Short title\nThis Act may be cited as the Prohibiting Political Prosecutions Act of 2026 .\n#### 2. Impermissible considerations for initiating or declining charges and right of action\n##### (a) In general\nChapter 31 of title 28, United States Code, is amended by adding at the end the following:\n530E. Impermissible considerations for initiating or declining charges and right of action (a) Definition In this section, the term applicable covered individual means\u2014 (1) if the investigation involved the Federal Bureau of Investigation, the Director of the Federal Bureau of Investigation, a special agent in charge, a section chief, and an agent of the Federal Bureau of Investigation; (2) if the investigation involved an agency other than the Federal Bureau of Investigation, the head of the agency and an agent of the agency; and (3) a United States attorney and a line prosecutor. (b) Impermissible considerations (1) In general In determining whether to commence or recommend prosecution or investigation an attorney or investigator for the Government shall not consider the political or policy associations, activities, or beliefs of the person. An attorney or investigator for the Government shall not commence or recommend prosecution or investigation against a person in order to influence or change, in any way, the political or policy associations, activities, or beliefs of the person. (2) Applications Each criminal complaint, information, indictment, and application for a search warrant or arrest warrant shall include an attestation by the applicable covered individual that\u2014 (A) the covered individual is not aware that the criminal complaint, information, indictment, search warrant, or arrest warrant, as applicable, is being sought because of the political association, activities, or beliefs of the person subject to the warrant or a defendant named in the indictment; (B) the covered individual is not aware that the criminal complaint, information, indictment, search warrant, or arrest warrant, as applicable, is being sought in order to influence or change, in any way, the political or policy associations, activities, or beliefs of the person subject to the warrant or a defendant named in the indictment; and (C) in the case of a criminal complaint, information, or indictment, the covered individual believes the evidence in support of the indictment is sufficient to prove the guilt of the defendant at trial beyond a reasonable doubt. (3) Rule of construction Nothing in paragraph (1) may be construed to limit the authority of the Attorney General\u2014 (A) to establish prosecutorial and other guidelines for personnel of the Department of Justice; (B) to displace any additional provisions of the Justice Manual; or (C) to exclude by implication any other consideration the Attorney General determines is impermissible in determining whether to commence or recommend prosecution or take other action against a person. (c) Right of action Any person investigated or prosecuted following a violation of this section may bring a civil action in an appropriate court of the United States for damages against any applicable covered individual in their individual capacity. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 31, United States Code, is amended by adding at the end the following:\n530E. Impermissible considerations for initiating or declining charges and right of action. .\n#### 3. Grand jury reforms\n##### (a) In general\nRule 6 of the Federal Rules of Criminal Procedure is amended by adding at the end the following:\n(j) Presentation of exculpatory information If the government is aware of exculpatory evidence, the government shall inform the grand jury of its nature and existence. (k) Presentation of impeachment information The government shall inform the grand jury of any statement, report, communication, or recording in the possession of the government made by, or including, a witness who testified before the grand jury that may impeach the credibility of the testimony of the witness. .\n##### (b) Discovery and inspection\nRule 16(a)(1) of the Federal Rules of Criminal Procedure is amended\u2014\n**(1)**\nby redesignating subparagraph (G) as subparagraph (H); and\n**(2)**\nby inserting after subparagraph (F) the following:\n(G) Grand jury vote tally Upon a defendant\u2019s request, the government must furnish the defendant with the number of grand jurors who voted to indict on each count and the number of grand jurors present for the vote. .\n##### (c) Dismissal\nRule 48 of the Federal Rules of Criminal Procedure is amended by adding at the end the following:\n(c) For political reasons (1) In general Upon a motion by the defendant alleging that substantial grounds exist to believe that the political or policy associations, activities, or beliefs of the defendant were considered in bringing the prosecution or that the prosecution was sought in order to influence or change, in any way, the political or policy association, activities, or beliefs of the defendant and requesting dismissal of all or part of the indictment and inspection of grand jury minutes, the judge shall review the grand jury minutes in camera, including whether\u2014 (A) the government provided the grand jury with sufficient evidence to prove by probable cause that the defendant committed each element of the crime; (B) the evidence presented to the grand jury was without impermissible reference to the political or policy associations, activities, or beliefs of the defendant; (C) the government informed the grand jury of the nature and existence of all exculpatory evidence of which the government was aware; and (D) the government informed the grand jury of any statement, report, communication, or recording in the possession of the government made by a witness who testified before the grand jury that may impeach the credibility of the grand jury testimony of the witness. (2) Dismissal of all or part of the indictment (A) Determination If the court determines that evidence presented to the grand jury impermissibly related to the political or policy associations, activities or beliefs of the defendant, or that the evidence was not sufficient to prove probable cause for each element of the offense, the court shall dismiss all or part of the indictment, as applicable. (B) Re-presentation If the court dismisses all or part of an indictment under this paragraph, the government may re-present a case to a different grand jury only if the government first files a motion providing, and the court first finds, substantial grounds to believe that the political or policy associations, activities, or beliefs of the target were not considered in bringing the prosecution and that the prosecution is not being sought in order to influence or change, in any way, the political or policy association, activities, or beliefs of the defendant. .\n#### 4. Prohibition on White House influence\n##### (a) In general\nChapter 31 of title 28, United States Code, as amended by section 2 of this Act, is amended by adding at the end the following:\n530F. Impermissible influence (a) In general No President or any employee of the White House shall directly or indirectly instruct the Department of Justice concerning investigative or charging decisions in individual criminal cases. (b) No consideration No Department of Justice employee may consider direct or indirect instructions from the President or any White House employee when making investigative or charging decisions in individual criminal cases. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 31, United States Code, as amended by section 2 of this Act, is amended by adding at the end the following:\n530F. Impermissible influence. .\n#### 5. Reporting\n##### (a) In general\nSection 530B of title 28, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) (1) All employees of the Department of Justice and Federal Bureau of Investigation shall report to the Office of Professional Responsibility of the Department of Justice and the Office of the Inspector General of the Department of Justice any instance where the political or policy associations, activities, or beliefs of the target were considered in any investigation or charging decision or when an investigation or charging decision was made in order to influence or change, in any way, the political or policy association, activities, or beliefs of the target. (2) The Director of the Office of Professional Responsibility of the Department of Justice and the Inspector General of the Department of Justice shall disclose to each appropriate congressional committee any communication or complaint received by the Office or Inspector General relating to an allegation that, in determining whether to commence or recommend prosecution or take other action against a person, the political or policy associations, activities, or beliefs of the person were considered or a decision was made in order to influence or change, in any way, the political or policy association, activities, or beliefs of the person. (3) Any disclosure made under paragraph (2) shall\u2014 (A) include\u2014 (i) the specific communication or complaint received by the Office of Professional Responsibility or Office of the Inspector General; (ii) the investigative steps the Office of Professional Responsibility or Office of the Inspector General took in response to the allegation; and (iii) any findings of the Office of Professional Responsibility or Office of the Inspector General; (B) notwithstanding section 552a of title 5, be confidential and not subject to disclosure; and (C) be made not later than 5 business days after the issuance of any findings or, if no findings are issued, be made no later than 5 business days after the conclusion of the investigation. (4) The Office of Professional Responsibility of the Department of Justice and the Office of the Inspector General of the Department of Justice shall investigate all communications and complaints relating to an allegation that, in determining whether to commence or recommend prosecution or take other action against a person, the political association, activities, or beliefs of the person were considered or a decision was made in order to influence or change, in any way, the political or policy associations, activities, or beliefs of the person. Such investigations shall be commenced not later than 5 business days after the initial receipt of the communication or complaint and shall be completed not later than 1 month after such receipt. .\n#### 6. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of the provisions of such to any person or circumstance shall not be affected thereby.",
      "versionDate": "2026-02-13",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3874",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prohibiting Political Prosecutions Act of 2026",
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
        "name": "Law",
        "updateDate": "2026-03-09T19:20:00Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7575ih.xml"
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
      "title": "Prohibiting Political Prosecutions Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prohibiting Political Prosecutions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T08:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to prohibit attorneys for the Government from being influenced by the political association, activities, or beliefs of a person in determining whether to commence or recommend prosecution or take other action against the person.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T08:33:32Z"
    }
  ]
}
```
