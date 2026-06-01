# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/798
- Title: Dignity for Aborted Children Act
- Congress: 119
- Bill type: HR
- Bill number: 798
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T21:53:11Z
- Update date including text: 2025-12-05T21:53:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/798",
    "number": "798",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Dignity for Aborted Children Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:53:11Z",
    "updateDateIncludingText": "2025-12-05T21:53:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:10:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr798ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 798\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Miller of Illinois (for herself, Mr. Babin , Mr. Moore of Alabama , Mr. Moore of West Virginia , Mr. Ogles , Mr. Webster of Florida , Mr. Harris of Maryland , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo protect the dignity of fetal remains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dignity for Aborted Children Act .\n#### 2. Constitutional authority\nCongress enacts the following pursuant to Congress\u2019 power under\u2014\n**(1)**\nthe Interstate Commerce Clause of section 8 of article I of the Constitution;\n**(2)**\nsection 5 of the 14th Amendment to the Constitution of the United States, including the power to enforce the prohibition on government action denying equal protection of the laws; and\n**(3)**\nsection 8 of article I of the Constitution of the United States to make all laws necessary and proper for the carrying into execution of powers vested by the Constitution in the Government of the United States.\n#### 3. Protection of fetal remains\n##### (a) In general\nPart H of title IV of the Public Health Service Act ( 42 U.S.C. 289 et seq. ) is amended by adding at the end the following:\n498F. Protection of fetal remains (a) Consent requirement (1) In general Any abortion provider, after performing an abortion, shall provide the patient with an informed consent form, offering the patient the following options for disposal of the human fetal tissue from the abortion: (A) The patient may take possession of the human fetal tissue and may choose to transfer the tissue to an entity providing interment or cremation services. (B) The patient may elect to release the human fetal tissue to the abortion provider, who shall be subject to the requirements of subsection (b). (2) Consent requirements An abortion provider described in paragraph (1) shall\u2014 (A) obtain a patient signature on each consent form required under paragraph (1); and (B) retain each such form in the patient's file. (b) Provider disposal requirement It shall be unlawful for any abortion provider who, after performing an abortion in which the woman on whom the abortion was performed elects, pursuant to subsection (a)(1)(B), to release the human fetal tissue to the abortion provider, to fail to provide for the final disposition of the human fetal tissue through interment or cremation, consistent with State law regarding the disposal of human remains, not later than 7 days after the date on which the abortion procedure was performed. Such final disposition of human fetal tissue may be carried out through interment or cremation of tissue from more than one abortion procedure collectively. (c) Penalties (1) Informed consent violations An abortion provider who fails to maintain the documentation required under subsection (a)(2)(B) shall be subject to civil monetary penalties in an amount not to exceed $50,000. (2) Disposal violations Any abortion provider who violates subsection (b) shall be fined in accordance with title 18, United States Code, imprisoned not more than 5 years, or both. (3) Bar to prosecution A patient upon whom an abortion in violation of subsection (b) is performed or attempted may not be prosecuted under, or for a conspiracy to violate, paragraph (1), or for an offense under section 2, 3, or 4 of title 18, United States Code, based on such a violation. (d) Reporting Each abortion provider described in subsection (a)(1) shall submit annual reports to the Secretary indicating, with respect to the reporting period\u2014 (1) the aggregate number of abortion procedures performed by such abortion provider; (2) the gestational age at the time of each such procedure; and (3) for abortions carried out using an abortion method other than chemical abortion, the aggregate number of fetal remains transferred for interment or cremation and the number released to patients. (e) Annual reports by the Secretary The Secretary shall submit to Congress an annual report on the number of abortions by State, procedure type, and method of disposal of human fetal tissue. (f) Non-Preemption Nothing in this section shall preempt any State requirement that, at a minimum, requires interment or cremation in the same manner that other human remains are required to be treated in such State. (g) Definitions In this section\u2014 (1) the term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability to produce a live birth and preserve the life and health of the child born alive; or (ii) to remove a dead unborn child; (2) the term abortion provider means an individual or entity that performs abortions; and (3) the term human fetal tissue has the meaning given the term in section 498A(g). .",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "242",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dignity for Aborted Children Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Cemeteries and funerals",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Census and government statistics",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-26T20:17:27Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-26T20:17:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T15:00:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr798",
          "measure-number": "798",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr798v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>"
        },
        "title": "Dignity for Aborted Children Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr798.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr798"
    },
    "title": "Dignity for Aborted Children Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dignity for Aborted Children Act</strong></p><p>This bill establishes\u00a0requirements for abortion providers with respect to\u00a0the disposal of human fetal tissue from an abortion.</p><p>Specifically, it requires abortion providers to obtain a patient's informed consent for one of two specified methods of disposition and to retain the corresponding documentation in the patient's file.</p><p>First, patients may choose to retain possession of the tissue. A patient may choose to transfer the tissue to an entity that provides interment or cremation services.</p><p>Second, patients may choose to release the tissue to the provider. Providers must ensure any tissue released to them is interred or cremated within seven days of the procedure in a manner consistent with state law regarding the disposal of human remains.</p><p>Abortion providers must submit reports annually to the Department of Health and Human Services about these requirements and other specified information.</p><p>The bill establishes civil penalties for violations of the requirement to retain documentation of informed consent,\u00a0and it establishes\u00a0criminal penalties for violations of the\u00a0requirement regarding the disposal of human fetal tissue.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr798"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr798ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect the dignity of fetal remains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:03:37Z"
    },
    {
      "title": "Dignity for Aborted Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dignity for Aborted Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:53:20Z"
    }
  ]
}
```
