# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/242?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/242
- Title: Dignity for Aborted Children Act
- Congress: 119
- Bill type: S
- Bill number: 242
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-12-05T21:53:17Z
- Update date including text: 2025-12-05T21:53:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/242",
    "number": "242",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Dignity for Aborted Children Act",
    "type": "S",
    "updateDate": "2025-12-05T21:53:17Z",
    "updateDateIncludingText": "2025-12-05T21:53:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T16:22:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SD"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MS"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WV"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s242is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 242\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Ricketts (for himself, Mr. Lankford , Mr. Sheehy , Mr. Banks , Mr. Daines , Mr. Risch , Mr. Rounds , Mr. Wicker , Mr. Schmitt , Mr. Justice , Mr. Tillis , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo protect the dignity of fetal remains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dignity for Aborted Children Act .\n#### 2. Constitutional authority\nCongress enacts the following pursuant to Congress\u2019 power under\u2014\n**(1)**\nthe Interstate Commerce Clause of section 8 of article I of the Constitution;\n**(2)**\nsection 5 of the 14th Amendment to the Constitution of the United States, including the power to enforce the prohibition on government action denying equal protection of the laws; and\n**(3)**\nsection 8 of article I of the Constitution of the United States to make all laws necessary and proper for the carrying into execution of powers vested by the Constitution in the Government of the United States.\n#### 3. Protection of fetal remains\n##### (a) In general\nPart H of title IV of the Public Health Service Act ( 42 U.S.C. 289 et seq. ) is amended by adding at the end the following:\n498F. Protection of fetal remains (a) Consent requirement (1) In general Any abortion provider, after performing an abortion, shall provide the patient with an informed consent form, offering the patient the following options for disposal of the human fetal tissue from the abortion: (A) The patient may take possession of the human fetal tissue and may choose to transfer the tissue to an entity providing interment or cremation services. (B) The patient may elect to release the human fetal tissue to the abortion provider, who shall be subject to the requirements of subsection (b). (2) Consent requirements An abortion provider described in paragraph (1) shall\u2014 (A) obtain a patient signature on each consent form required under paragraph (1); and (B) retain each such form in the patient's file. (b) Provider disposal requirement It shall be unlawful for any abortion provider who, after performing an abortion in which the woman on whom the abortion was performed elects, pursuant to subsection (a)(1)(B), to release the human fetal tissue to the abortion provider, to fail to provide for the final disposition of the human fetal tissue through interment or cremation, consistent with State law regarding the disposal of human remains, not later than 7 days after the date on which the abortion procedure was performed. Such final disposition of human fetal tissue may be carried out through interment or cremation of tissue from more than one abortion procedure collectively. (c) Penalties (1) Informed consent violations An abortion provider who fails to maintain the documentation required under subsection (a)(2)(B) shall be subject to civil monetary penalties in an amount not to exceed $50,000. (2) Disposal violations Any abortion provider who violates subsection (b) shall be fined in accordance with title 18, United States Code, imprisoned not more than 5 years, or both. (3) Bar to prosecution A patient upon whom an abortion in violation of subsection (b) is performed or attempted may not be prosecuted under, or for a conspiracy to violate, paragraph (1), or for an offense under section 2, 3, or 4 of title 18, United States Code, based on such a violation. (d) Reporting Each abortion provider described in subsection (a)(1) shall submit annual reports to the Secretary indicating, with respect to the reporting period\u2014 (1) the aggregate number of abortion procedures performed by such abortion provider; (2) the gestational age at the time of each such procedure; and (3) for abortions carried out using an abortion method other than chemical abortion, the aggregate number of fetal remains transferred for interment or cremation and the number released to patients. (e) Annual reports by the Secretary The Secretary shall submit to Congress an annual report on the number of abortions by State, procedure type, and method of disposal of human fetal tissue. (f) Non-Preemption Nothing in this section shall preempt any State requirement that, at a minimum, requires interment or cremation in the same manner that other human remains are required to be treated in such State. (g) Definitions In this section\u2014 (1) the term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability to produce a live birth and preserve the life and health of the child born alive; or (ii) to remove a dead unborn child; (2) the term abortion provider means an individual or entity that performs abortions; and (3) the term human fetal tissue has the meaning given the term in section 498A(g). .",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "798",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dignity for Aborted Children Act",
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
            "name": "Abortion",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Cemeteries and funerals",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Census and government statistics",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-26T20:17:12Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-26T20:17:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:20:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s242",
          "measure-number": "242",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s242v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>"
        },
        "title": "Dignity for Aborted Children Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s242.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s242"
    },
    "title": "Dignity for Aborted Children Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s242"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s242is.xml"
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
      "title": "Dignity for Aborted Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dignity for Aborted Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the dignity of fetal remains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:30Z"
    }
  ]
}
```
