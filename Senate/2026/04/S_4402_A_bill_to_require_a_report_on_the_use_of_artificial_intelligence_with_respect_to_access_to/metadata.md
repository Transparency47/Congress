# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4402
- Title: A bill to require a report on the use of artificial intelligence with respect to access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4402
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-08T20:39:07Z
- Update date including text: 2026-05-08T20:39:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4402",
    "number": "4402",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A bill to require a report on the use of artificial intelligence with respect to access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-08T20:39:07Z",
    "updateDateIncludingText": "2026-05-08T20:39:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
        "item": {
          "date": "2026-04-27T22:53:59Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4402is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4402\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require a report on the use of artificial intelligence with respect to access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978, and for other purposes.\n#### 1. Definition of artificial intelligence\nIn this Act, the term artificial intelligence has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n#### 2. Report on use of artificial intelligence\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Attorney General and the Director of National Intelligence shall jointly submit to the entities and individuals specified in subsection (c) a report describing all use of artificial intelligence with access to unminimized information collected pursuant to any section of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 et seq. ).\n##### (b) Contents\nThe report required by subsection (a) shall include, for each use of artificial intelligence included in the report, the following:\n**(1)**\nThe name of the artificial intelligence system, if applicable, and a description of its use, function, and purpose.\n**(2)**\nA description of the testing and evaluation process prior to adoption, as well as the process for continuous monitoring of the system\u2019s performance, including a description of mechanisms and protocols for continuous human review.\n**(3)**\nAn identification of the entity, whether an office within a government agency or a private entity, that developed, trained, initiated the training of, or intentionally modified the artificial intelligence system.\n**(4)**\nA description of the data used to train or fine-tune the artificial intelligence system, including a description of the fitness of the selected model and its training data for the functions described in paragraph (1), as well as any stated limitations of the selected model indicated in documentation associated with the selected model.\n**(5)**\nAn identification of\u2014\n**(A)**\nwhen the artificial intelligence system was initially allowed access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 et seq. );\n**(B)**\nwhat access the artificial intelligence system has to that information; and\n**(C)**\nany additional data sources the artificial intelligence system uses for operation in the functions identified in paragraph (1).\n**(6)**\nWhether the use of the artificial intelligence system has previously been reported to the entities and individuals specified in subsection (c) and, if so, whether the Foreign Intelligence Surveillance Court has issued any orders or opinions regarding the use of the artificial intelligence, including as part of minimization or targeting procedures.\n**(7)**\nAny additional information determined necessary by the Attorney General or the Director of National Intelligence.\n##### (c) Entities and individuals specified\nThe entities and individuals specified in this subsection are\u2014\n**(1)**\nthe congressional intelligence committees (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ));\n**(2)**\nthe Committee on the Judiciary of the Senate;\n**(3)**\nthe Committee on the Judiciary of the House of Representatives;\n**(4)**\nthe presiding judge of the Foreign Intelligence Surveillance Court; and\n**(5)**\nthe presiding judge of the Foreign Intelligence Surveillance Court of Review.\n##### (d) Form\nThe report required by subsection (a) shall be submitted in unclassified and classified form.\n##### (e) Public availability\nThe unclassified version of the report required by subsection (a) shall be made publicly available on the websites of the Department of Justice and the Office of the Director of National Intelligence.\n#### 3. Requirement relating to use of artificial intelligence\nBefore providing any future artificial intelligence system with access to unminimized information collected pursuant to any section of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 et seq. ), the Attorney General and the Director of National Intelligence shall jointly provide to the entities and individuals specified in section 2(c) the following:\n**(1)**\nA notification describing the proposed name, function, and access to information of the artificial intelligence system.\n**(2)**\nAn assessment of whether such use of the artificial intelligence complies with the Foreign Intelligence Surveillance Act, existing procedures or opinions adopted or issued by the Foreign Intelligence Surveillance Court, and any other applicable laws, directives, and regulations.",
      "versionDate": "2026-04-27",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-08T20:39:07Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4402is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report on the use of artificial intelligence with respect to access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:30Z"
    },
    {
      "title": "A bill to require a report on the use of artificial intelligence with respect to access to unminimized information collected pursuant to the Foreign Intelligence Surveillance Act of 1978, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T10:56:39Z"
    }
  ]
}
```
