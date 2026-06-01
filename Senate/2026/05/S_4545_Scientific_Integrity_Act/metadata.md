# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4545
- Title: Scientific Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 4545
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-22T02:23:26Z
- Update date including text: 2026-05-22T02:23:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4545",
    "number": "4545",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Scientific Integrity Act",
    "type": "S",
    "updateDate": "2026-05-22T02:23:26Z",
    "updateDateIncludingText": "2026-05-22T02:23:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T18:42:08Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NH"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4545is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4545\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Schatz (for himself, Mr. Bennet , Mr. Blumenthal , Mr. Hickenlooper , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mr. Padilla , Ms. Rosen , Mr. Schiff , Mr. Van Hollen , Mr. Warner , Mr. Welch , Mr. Whitehouse , Mr. Wyden , Mrs. Shaheen , Mr. Schumer , Mr. Booker , Ms. Warren , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the America COMPETES Act to establish certain scientific integrity policies for Federal agencies that fund, conduct, or oversee scientific research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scientific Integrity Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nscience and the scientific process should help inform and guide public policy decisions on a wide range of issues, including improvement of public health, protection of the environment, and protection of national security;\n**(2)**\nthe public must be able to trust the science and scientific process informing public policy decisions;\n**(3)**\nscience, the scientific process, and the communication of science should be free from politics, ideology, and financial conflicts of interest;\n**(4)**\npolicies and procedures that ensure the integrity of the conduct and communication of publicly funded science are critical to ensuring public trust;\n**(5)**\na Federal agency that funds, conducts, or oversees research should not suppress, alter, interfere with, or otherwise impede the timely communication and open exchange of data and findings to other agencies, policymakers, and the public of research conducted by a scientist or engineer employed or contracted by a Federal agency that funds, conducts, or oversees scientific research;\n**(6)**\nFederal agencies that fund, conduct, or oversee research should work to prevent the suppression or distortion of the data and findings;\n**(7)**\nunder the First Amendment to the Constitution of the United States, citizens of the United States have the right to petition the government for a redress of grievances ; and\n**(8)**\nCongress has further protected those rights under section 7211 of title 5, United States Code, which states, [t]he right of employees, individually or collectively, to petition Congress or a member of Congress . . . may not be interfered with or denied .\n#### 3. Amendment to America COMPETES Act\nSection 1009 of the America COMPETES Act ( 42 U.S.C. 6620 ) is amended by striking subsections (a) and (b) and inserting the following:\n(a) Scientific integrity policies (1) In general Not later than 90 days after the date of the enactment of the Scientific Integrity Act , the head of each covered agency shall\u2014 (A) adopt and enforce a scientific integrity policy in accordance with subsections (b) and (c); and (B) submit such policy to the Director of the Office of Science and Technology Policy for approval. (2) Publication Not later than 30 days after the Director of the Office of Science and Technology Policy approves the scientific integrity policy under paragraph (1) with respect to a covered agency, the head of that agency shall\u2014 (A) make such policy available to the public on the website of the agency; and (B) submit such policy to the relevant Committees of Congress. (b) Requirements A scientific integrity policy under subsection (a) for a covered agency\u2014 (1) shall prohibit any covered individual from\u2014 (A) engaging in dishonesty, fraud, deceit, misrepresentation, coercive manipulation, or other scientific or research misconduct; (B) suppressing, altering, interfering with, delaying without scientific merit, or otherwise impeding the release and communication of, scientific or technical findings; (C) intimidating or coercing an individual to alter or censor, attempting to intimidate or coerce an individual to alter or censor, or retaliating against an individual for failure to alter or censor, scientific or technical findings; or (D) implementing an institutional barrier to cooperation with scientists outside the covered agency and the timely communication of scientific or technical findings; (2) shall allow a covered individual to\u2014 (A) disseminate scientific or technical findings, subject to existing law, by\u2014 (i) participating in scientific conferences; and (ii) seeking publication in online and print publications through peer-reviewed, professional, or scholarly journals; (B) sit on scientific advisory or governing boards; (C) join or hold leadership positions on scientific councils, societies, unions, and other professional organizations; (D) contribute to the academic peer-review process as reviewers or editors; and (E) participate and engage with the scientific community; (3) may require a covered individual, before disseminating scientific or technical findings as described in paragraph (2)(A), to submit such findings to the agency for the purpose of review by the agency of the data and findings for technical accuracy if the scientific integrity policy outlines a clear and consistent process for such review; and (4) shall require that\u2014 (A) scientific conclusions are not made based on political considerations; (B) the selection and retention of candidates for science and technology positions in the covered agency are based primarily on the candidate\u2019s expertise, scientific credentials, experience, and integrity; (C) personnel actions regarding covered individuals, except for political appointees, are not taken on the basis of political consideration or ideology; (D) covered individuals adhere to the highest ethical and professional standards in conducting their research and disseminating their findings; (E) appropriate rules, procedures, and safeguards are in place to ensure the integrity of the scientific process within the covered agency; (F) scientific or technological information considered in policy decisions is subject to well-established scientific processes, including peer review as appropriate; (G) procedures, including procedures with respect to applicable whistleblower protections, are in place as necessary to ensure the integrity of scientific and technological information and processes on which the covered agency relies in its decisionmaking or that the covered agency otherwise uses; and (H) enforcement of such policy is consistent with the processes for an administrative hearing and an administrative appeal. (c) Implementation In carrying out subsection (a), the head of each covered agency shall\u2014 (1) design the scientific integrity policy under such subsection to apply with respect to the covered agency; (2) ensure that such policy is clear with respect to what activities are permitted and what activities are not permitted; (3) ensure that there is a process for individuals not employed or contracted by the agency, including grantees, collaborators, partners, and volunteers, to report violations of the scientific integrity policy; (4) enforce such policy uniformly throughout the covered agency; and (5) make such policy available to the public, employees, private contractors, and grantees of the covered agency. (d) Scientific Integrity Officer Not later than 90 days after the date of the enactment of the Scientific Integrity Act , each covered agency shall appoint a Scientific Integrity Officer, who shall\u2014 (1) be a career employee at the covered agency in a professional position; (2) have technical knowledge and expertise in conducting and overseeing scientific research; (3) direct the activities and duties described in subsections (e), (f), and (g); and (4) work closely with the inspector general of the covered agency, as appropriate. (e) Administrative process and training Not later than 180 days after the date of the enactment of the Scientific Integrity Act , the head of each covered agency shall establish\u2014 (1) an administrative process and administrative appeal process for dispute resolution consistent with the scientific integrity policy of the covered agency adopted under subsection (a); and (2) a training program to provide\u2014 (A) regular scientific integrity and ethics training to employees and contractors of the covered agency; (B) training to new employees of the covered agency who are covered individuals within 1 month of commencing employment; (C) information to ensure that covered individuals are fully aware of their rights and responsibilities regarding the conduct of scientific research, publication of scientific research, and communication with the media and the public regarding scientific research; and (D) information to ensure that covered individuals are fully aware of their rights and responsibilities for administrative hearings and appeals established in the scientific integrity policy of the covered agency. (f) Reporting (1) Annual report Each year, each Scientific Integrity Officer appointed by a covered agency under subsection (d) shall post an annual report on the public website of the covered agency that includes, for the year covered by the report\u2014 (A) the number of complaints of misconduct with respect to the scientific integrity policy adopted under subsection (a)\u2014 (i) filed for administrative redress; (ii) petitioned for administrative appeal; and (iii) still pending from years prior to the year covered by the report, if any; (B) an anonymized summary of each such complaint and the results of each such complaint; and (C) any changes made to the scientific integrity policy. (2) Incident report (A) In general Not later than 30 days after the date on which an incident described in subparagraph (B) occurs, the head of a covered agency shall submit a report describing the incident to the Office of Science and Technology Policy and the relevant Committees of Congress. (B) Incident An incident described in this subparagraph is an incident in which an individual, acting outside the channels established under subsection (e), overrules the decision of the Scientific Integrity Officer appointed under subsection (d) with respect to a dispute regarding a violation of the scientific integrity policy adopted under subsection (a). (g) Office of Science and Technology Policy The Director of the Office of Science and Technology Policy shall\u2014 (1) collate, organize, and publicly share all information received by the Director under subsection (f) in 1 place on the website of the Office of Science and Technology Policy; and (2) on an annual basis, convene the Scientific Integrity Officer of each covered agency appointed under subsection (d) to discuss best practices for implementing the requirements of this section. (h) Periodic review and approval (1) Internal review The head of each covered agency shall periodically conduct a review of the scientific integrity policy adopted under subsection (a) and change such policy as appropriate. (2) Review by the Office of Science and Technology Policy (A) Review of substantial updates The head of each covered agency shall submit to the Office of Science and Technology Policy for approval any substantial changes to the scientific integrity policy adopted under subsection (a). (B) Quinquennial review Not later than 5 years after the date of the enactment of the Scientific Integrity Act , and every 5 years thereafter, the head of each covered agency shall submit the scientific integrity policy for such agency to the Office of Science and Technology Policy for review and approval. (i) Comptroller General review Not later than 2 years after the date of the enactment of the Scientific Integrity Act , the Comptroller General of the United States shall conduct a review of the implementation of the scientific integrity policy by each covered agency. (j) Definitions In this section: (1) Agency The term agency has the meaning given the term in section 551 of title 5, United States Code. (2) Covered agency The term covered agency means an agency that funds, conducts, or oversees scientific research. (3) Covered individual The term covered individual means a Federal employee or contractor who\u2014 (A) is engaged in, supervises, or manages scientific activities; (B) analyzes or publicly communicates information resulting from scientific activities; or (C) uses scientific information or analyses in making bureau, office, or agency policy, management, or regulatory decisions. (4) Relevant committees of Congress The term relevant Committees of Congress means\u2014 (A) the Committee on Commerce, Science, and Transportation of the Senate; and (B) the Committee on Science, Space, and Technology of the House of Representatives. .\n#### 4. Existing policies; clarification\n##### (a) Existing scientific integrity policies\nNotwithstanding the amendments made by this Act, the scientific integrity policy of a covered agency that was in effect on the day before the date of the enactment of this Act may satisfy the requirements under the amendments made by this Act if the head of the covered agency\u2014\n**(1)**\nmakes a written determination that the policy satisfies such requirements; and\n**(2)**\nsubmits the written determination and the policy to the Director of the Office of Science and Technology Policy for review and approval.\n##### (b) Clarification\nNothing in this Act or the amendments made by this Act shall affect the application of United States copyright law.\n##### (c) Covered agency defined\nThe term covered agency has the meaning given the term in section 1009 of the America COMPETES Act ( 42 U.S.C. 6620 ), as amended by section 3.",
      "versionDate": "2026-05-14",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4545is.xml"
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
      "title": "Scientific Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Scientific Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the America COMPETES Act to establish certain scientific integrity policies for Federal agencies that fund, conduct, or oversee scientific research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:28Z"
    }
  ]
}
```
